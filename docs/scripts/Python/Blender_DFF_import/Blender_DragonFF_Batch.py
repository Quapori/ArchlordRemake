import math

import bpy
import os

# === Path to the root of the source folder (recursive) ===
root_path = "D:/Mesh/Object"

# root_path = "D:/ARCHLORD/Test"

# === Import DFF with default settings ===
def import_dff_operator(file_path):
    bpy.ops.import_scene.dff(
        filepath=file_path,
        load_txd=False,
        image_ext="PNG",
        group_materials=True,
        connect_bones=False,
        materials_naming="TEX"
    )


# === Clear the scene ===
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

    # in case the world shader was modified
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()

def add_prefix_to_materials(prefix="MAT_"):
    for mat in bpy.data.materials:
        if not mat.name.startswith(prefix):
            old_name = mat.name
            mat.name = prefix + mat.name
            print(f"✅ Renamed: {old_name} → {mat.name}")
        else:
            print(f"⏭️ Already prefixed: {mat.name}")

def proof_and_clean_uvs():
    for mesh in bpy.data.meshes:
        for uv_layer in mesh.uv_layers:
            for loop in mesh.loops:
                uv = uv_layer.data[loop.index].uv
                if math.isnan(uv.x) or math.isnan(uv.y):
                    print(f"⚠️ NaN-UVs found in Mesh '{mesh.name}' → Set to (0.0, 0.0)")
                    uv_layer.data[loop.index].uv = (0.0, 0.0)

def set_rotation_x_to_one():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.rotation_mode = 'QUATERNION'
            obj.rotation_quaternion[1] = 1.0  # X-component
    print("🔄 All meshes: rotation_quaternion[X] set to 1.0")


def replace_collection_with_export(dff_name):
    old_coll_name = os.path.basename(dff_name)  # e.g. "auto.dff"

    # 1. Delete "Export" collection if it exists
    if "Export" in bpy.data.collections:
        old_export = bpy.data.collections["Export"]
        bpy.data.collections.remove(old_export)
        print("🗑️ Old 'Export' collection deleted.")

    # 2. Find DFF collection and rename it
    if old_coll_name in bpy.data.collections:
        coll = bpy.data.collections[old_coll_name]
        coll.name = "Export"
        print(f"✏️ Collection '{old_coll_name}' renamed to 'Export'.")
    else:
        print(f"⚠️ Collection '{old_coll_name}' not found.")


# === Main function with progress output ===
def batch_import_dffs(root_dir):
    dff_files = []

    # 1. Collect all .dff files
    for folder_path, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".dff"):
                dff_path = os.path.join(folder_path, file)
                dff_files.append(dff_path)

    total = len(dff_files)
    print(f"\n🔄 Starting import of {total} DFF files...\n")

    # 2. Process each with counter
    for index, dff_path in enumerate(dff_files, start=1):
        print(f"[{index}/{total}] 📥 Importing: {dff_path}")

        try:
            import_dff_operator(dff_path)
            replace_collection_with_export(os.path.basename(dff_path))
            set_rotation_x_to_one()
            add_prefix_to_materials()
            proof_and_clean_uvs()
        except Exception as e:
            print(f"❌ Error during import: {e}")
            continue

        blend_target = dff_path.replace(".dff", ".blend")
        fbx_target = dff_path.replace(".dff", ".fbx")
        bpy.ops.wm.save_as_mainfile(filepath=blend_target)
        print(f"✅ Saved as: {blend_target}\n")

        # FBX Export for UE5
        bpy.ops.export_scene.fbx(filepath=fbx_target,
                                 check_existing=True, filter_glob='*.fbx',
                                 use_selection=False, use_visible=False, use_active_collection=False, global_scale=1.0,
                                 apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True,
                                 bake_space_transform=False,
                                 object_types={'MESH', 'OTHER'},
                                 use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='FACE',
                                 colors_type='SRGB', prioritize_active_color=False, use_subsurf=False,
                                 use_mesh_edges=False,
                                 use_tspace=False, use_triangles=False, use_custom_props=False, add_leaf_bones=True,
                                 primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False,
                                 armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True,
                                 bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True,
                                 bake_anim_force_startend_keying=True, bake_anim_step=1.0,
                                 bake_anim_simplify_factor=1.0,
                                 path_mode='COPY', embed_textures=True, batch_mode='OFF', use_batch_own_dir=True,
                                 use_metadata=True, axis_forward='X', axis_up='Z')

        cleanup_file()

    print("\n✅ All DFF files processed successfully.\n")


# === START EXECUTION ===
batch_import_dffs(root_path)
