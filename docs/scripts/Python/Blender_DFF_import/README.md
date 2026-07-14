# DFF to FBX Batch Converter (Blender 3.6 + DragonFF)

This Python script is designed for **batch converting .dff (RenderWare)** 3D models into **.blend** and **.fbx** files using **Blender 3.6**. It leverages the [DragonFF plugin](https://github.com/Parik27/DragonFF) to import DFF files and is ideal for game developers or modders working with assets from legacy engines like **GTA** or **Archlord**.

---

## 📦 Features
- Recursively imports all `.dff` files from a specified root folder
- Cleans up the Blender scene before and after each import
- Rotates meshes by modifying quaternion X rotation for consistency
- Renames imported collections to a unified "Export" name
- Saves each model as `.blend`, then exports as `.fbx`
- Ready-to-use in **Unreal Engine 5** with correct axis and texture settings

---

## ✅ Requirements
- **Blender 3.6**
- **DragonFF Blender Plugin** (for `.dff` import)

Install DragonFF:
1. Download from: https://github.com/Parik27/DragonFF
2. In Blender: `Edit > Preferences > Add-ons > Install` → select DragonFF `.zip`

---

## 🧠 Script Logic

### 1. `import_dff_operator(file_path)`
Calls the DragonFF importer with preset options (e.g., PNG textures, grouped materials).

### 2. `purge_orphans()` & `cleanup_file()`
Cleans up the scene between each import: deletes all objects, collections, worlds, and orphan data blocks.

### 3. `set_rotation_x_to_one()`
Ensures all mesh objects have a quaternion X component set to 1.0 for orientation consistency.

### 4. `replace_collection_with_export(dff_name)`
Renames the imported collection (named after the DFF file) to `Export`. Removes any old collection with the same name to avoid conflicts.

### 5. `batch_import_dffs(root_dir)`
Main loop:
- Finds all `.dff` files
- Imports and processes each
- Saves `.blend` and exports `.fbx`
- Cleans scene for next import

---

## 📁 File Naming
Each `.dff` file will generate:
- A `.blend` file (same folder)
- A `.fbx` file (same folder)
- (Optional) `.usdc` path is pre-defined, but not currently used

---

## 🚀 Getting Started

1. Set your root folder path in the script:
```python
root_path = "D:/Mesh/Object"
```
2. Open the script in Blender's Text Editor
3. Run the script with `Run Script`

The script will recursively search all subfolders and process each `.dff` it finds.

---

## 🛠 FBX Export Settings
- Axis: Forward `X`, Up `Z`
- Scale: 1:1
- Texture: Embedded
- Mesh Modifiers: Applied
- Animations: Baked

These settings are compatible with Unreal Engine 5 by default.

---

## ⚠ Known Issues
If FBX export fails due to `NaN` values in UV maps:
- This can happen with corrupted or incomplete `.dff` files
- You can fix this by writing a UV validation function that checks for `NaN` values and replaces them

Let us know if you want that added to the script.

---

## 📜 License
This script is provided as-is, and you are free to modify and use it in your own projects.

