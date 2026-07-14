import os
import bpy
import json
import glob

from bpy.props import BoolProperty, StringProperty, PointerProperty
from bpy.types import Operator, Panel, Menu, PropertyGroup
from bpy_extras.io_utils import ImportHelper

bl_info = {
    "name": "Terrain Importer",
    "author": "Baloralys",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "Topbar",
    "description": "Importiert Terrain aus JSON-Dateien",
    "warning": "",
    "category": "Import-Export",
}


class TerrainImporterSettings(PropertyGroup):
    build_material: BoolProperty(name="Material erstellen?", default=True)
    build_continent: BoolProperty(name="Kontinent erstellen?", default=False)
    texture_path: StringProperty(name="Textur-Ordner", subtype='DIR_PATH', default="")
    blend_save_path: StringProperty(name="Speicherort Blender-Datei", subtype='DIR_PATH', default="")
    json_folder: StringProperty(name="Json-Ordner", subtype='DIR_PATH', default="")


"""global variables for batch processing of terrain + textures."""
collection_name = "Export"
uv_names = ["UVBase", "UVAlpha1", "UVColor1", "UVAlpha2", "UVColor2"]
uv_keys = ['uvbase', 'uvalpha1', 'uvcolor1', 'uvalpha2', 'uvcolor2']


def console_print(data):
    """Print data to the Blender console."""
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")


def purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
    else:
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()


def cleanup_file():
    """Remove all imported data associated with a file name."""
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


def save_and_export(blend_file, blender_file_dest_path):
    """Save the current Blender file to a specific directory."""
    save_path = os.path.join(blender_file_dest_path, f"{blend_file}.blend")
    bpy.ops.wm.save_as_mainfile(filepath=save_path)


def join_objects():
    """Join all meshes in the scene into one object."""
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
    bpy.ops.object.join()


def generate_material_name(textures):
    """Generate a material name based on the texture names in the JSON."""
    texture_names = [os.path.splitext(tex)[0] for tex in textures if tex]  # Omit empty texture slots
    return "MAT_" + "_".join(texture_names)


def create_material(textures, texture_path):
    # Generate material name
    material_name = generate_material_name(textures)

    # Create the material
    mat = bpy.data.materials.get(material_name)
    if not mat:
        mat = bpy.data.materials.new(name=material_name)
        mat.use_nodes = True

        links = mat.node_tree.links
        bsdf = mat.node_tree.nodes.get("Principled BSDF")

        # Create texture nodes
        tex_nodes = []
        possible_extensions = [".tga", ".png", ".dds", ".jpg", ".bmp", ".tif"]
        for idx, texture_name in enumerate([t for t in textures if t]):
            tex_node = mat.node_tree.nodes.new("ShaderNodeTexImage")
            # Entferne die Dateiendung, falls vorhanden
            texture_name = os.path.splitext(texture_name)[0]
            # Prüfe verschiedene Dateiendungen
            image = None
            for ext in possible_extensions:
                tex_path = os.path.join(texture_path, texture_name + ext)
                if os.path.exists(tex_path):
                    image = bpy.data.images.get(texture_name) or bpy.data.images.load(tex_path)
                    break

            if image:
                tex_node.image = image
            else:
                console_print(f"Texture missing: {texture_name} (checked: {', '.join(possible_extensions)})")

            # UV Node
            uv_node = mat.node_tree.nodes.new("ShaderNodeUVMap")
            uv_node.uv_map = uv_names[idx]

            # Connect UV -> Texture
            links.new(uv_node.outputs[0], tex_node.inputs[0])
            tex_nodes.append(tex_node)

        # Combine textures using MixRGB nodes
        final_output = None
        if len(tex_nodes) == 1:
            final_output = tex_nodes[0]
        elif len(tex_nodes) >= 3:
            mix_node = mat.node_tree.nodes.new("ShaderNodeMixRGB")
            links.new(mix_node.inputs[0], tex_nodes[1].outputs["Color"])  # Alpha
            links.new(mix_node.inputs[1], tex_nodes[0].outputs["Color"])  # Base
            links.new(mix_node.inputs[2], tex_nodes[2].outputs["Color"])  # Color1
            final_output = mix_node
        if len(tex_nodes) == 5:
            mix_node2 = mat.node_tree.nodes.new("ShaderNodeMixRGB")
            links.new(mix_node2.inputs[0], tex_nodes[3].outputs["Color"])  # Alpha2
            links.new(mix_node2.inputs[1], final_output.outputs["Color"])  # Previous mix
            links.new(mix_node2.inputs[2], tex_nodes[4].outputs["Color"])  # Color2
            final_output = mix_node2

        # Connect final output to Base Color
        if final_output:
            links.new(bsdf.inputs["Base Color"], final_output.outputs["Color"])

    # Assign material to object
    return mat


def import_terrain(filepath, json_filename, build_material, texture_path):
    """Import terrain from a JSON file and create a Blender scene."""
    # Open and parse JSON file
    with open(filepath, "r") as f:
        data = json.load(f)

    # Überprüfen, ob die Collection schon existiert
    if collection_name in bpy.data.collections:
        # Vorhandene Collection auswählen
        collection = bpy.data.collections[collection_name]
        print(f"verarbeite '{json_filename}'.")
        print(f"Collection '{collection_name}' bereits vorhanden und ausgewählt.")
    else:
        # Neue Collection erstellen
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)
        print(f"verarbeite '{json_filename}'.")
        print(f"Neue Collection '{collection_name}' erstellt und verlinkt.")

    split_index = 0
    for i, split in data['splits'].items():
        vertices = []
        edges = []
        faces = []

        # Convert and scale vertices
        for v in split['vertices']:
            vertices.append((v[0] / 100.0, v[2] / -100.0, v[1] / 100.0))

        # Create faces
        for face in split['faces']:
            faces.append((face[0], face[1], face[2]))

        # Create mesh and object
        mesh = bpy.data.meshes.new(name=f"TerrainMesh_{split_index}")
        mesh.from_pydata(vertices, edges, faces)
        obj = bpy.data.objects.new(f"{json_filename}_{split_index}", mesh)
        collection.objects.link(obj)

        # Create and load UV layers

        for uv_name, uv_key in zip(uv_names, uv_keys):
            if uv_key in split:
                uv_layer = obj.data.uv_layers.new(name=uv_name)
                for loop in obj.data.loops:
                    uv_layer.data[loop.index].uv = (
                        split[uv_key][loop.vertex_index][0],
                        -split[uv_key][loop.vertex_index][1]
                    )

        if build_material:
            # Assign material to object
            obj.active_material = create_material(split['textures'], texture_path)
            # entferne den Index im namen des Mesh und nenne ihn um mit dem dateinamen
        obj.name = json_filename
        obj.data.name = json_filename

        split_index += 1


class ImportTerrainOperator(Operator):
    bl_idname = "import_scene.terrain"
    bl_label = "Import Terrain"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cleanup_file()
        settings = context.scene.terrain_importer_settings
        texture_path = settings.texture_path
        blender_file_dest_path = settings.blend_save_path

        blend_files = set(os.path.splitext(os.path.basename(f))[0] for f in
                          glob.glob(os.path.join(blender_file_dest_path, "*.blend")))

        list_json_files = [
            f for f in sorted(glob.glob(os.path.join(settings.json_folder, "*.json")))
            if os.path.splitext(os.path.basename(f))[0] not in blend_files
        ]

        #list_json_files = sorted(glob.glob(os.path.join(settings.json_folder, "*.json")))
        build_material = settings.build_material
        build_continent = settings.build_continent

        if not list_json_files:
            self.report({'ERROR'}, "Keine JSON-Dateien gefunden!")
            return {'CANCELLED'}

        for json_file in list_json_files:
            file_name = os.path.splitext(os.path.basename(json_file))[0]
            import_terrain(json_file, file_name, build_material, texture_path)
            join_objects()
            if not build_continent:
                save_and_export(file_name, blender_file_dest_path)
                cleanup_file()

        return {'FINISHED'}


class TOPBAR_MT_terrain_menu(Menu):
    bl_label = "Terrain Importer"
    bl_idname = "TOPBAR_MT_terrain_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.call_panel", text="Einstellungen öffnen").name = "VIEW3D_PT_terrain_settings"


class VIEW3D_PT_terrain_settings(Panel):
    #bl_options = {'DEFAULT_CLOSED'}  # Panel wird breiter dargestellt
    bl_label = "Terrain Importer Einstellungen"
    bl_idname = "VIEW3D_PT_terrain_settings"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        #layout.ui_units_x = 50
        settings = context.scene.terrain_importer_settings

        layout.prop(settings, "build_material")
        layout.prop(settings, "build_continent")
        layout.prop(settings, "texture_path")
        layout.prop(settings, "blend_save_path")
        layout.prop(settings, "json_folder")

        layout.operator("import_scene.terrain", text="Import starten")


# Registration
classes = [TerrainImporterSettings, ImportTerrainOperator, TOPBAR_MT_terrain_menu, VIEW3D_PT_terrain_settings]

def menu_func(self, context):
    self.layout.menu(TOPBAR_MT_terrain_menu.bl_idname)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.terrain_importer_settings = PointerProperty(type=TerrainImporterSettings)
    bpy.types.TOPBAR_MT_editor_menus.append(menu_func)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.terrain_importer_settings
    bpy.types.TOPBAR_MT_editor_menus.remove(menu_func)

if __name__ == "__main__":
    register()
