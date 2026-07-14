# Terrain Importer for Blender

This Blender add-on is designed to import terrain data from JSON files into Blender. The terrain data is parsed from JSON files created using the tool found in the [Archlord repository](https://github.com/osiy1996/archlord). These JSON files contain information about terrain meshes, textures, and UV mappings, which are imported into Blender to create terrain models.

## Features

- Import terrain data from JSON files.
- Generate materials based on texture data in the JSON.
- Supports multiple UV maps (UVBase, UVAlpha1, UVColor1, UVAlpha2, UVColor2).
- Option to create and save a new Blender file with the imported terrain.
- Option to build continent-specific data.

## Requirements

- Blender 3.6.0 or higher.
- JSON files generated using the tool from the [Archlord repository](https://github.com/osiy1996/archlord).
- Texture files (in formats like `.png`, `.jpg`, `.tga`, etc.) associated with the terrain.

## Installation

1. Download or clone this repository.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click `Install...` and select the `.zip` file of this repository.
4. Enable the "Terrain Importer" add-on.

## Setup

1. After enabling the add-on, you will find the "Terrain Importer" settings in the "Properties" panel under the "Scene" tab.
2. Configure the following settings:
   - **Material Creation**: Enable this to create materials for the terrain objects.
   - **Continent Creation**: Enable this to create continent-specific terrain data.
   - **Texture Folder**: Provide the folder where your terrain textures are stored.
   - **Blender Save Path**: Specify the folder where the Blender files will be saved.
   - **JSON Folder**: Set the folder where your JSON files are stored.

## Usage

1. Ensure that the required JSON files are located in the folder specified in the "JSON Folder" setting. These files should be generated using the [Archlord tool](https://github.com/osiy1996/archlord).
2. Click the "Import Terrain" button to import the terrain data. The plugin will process all the JSON files in the specified folder and create corresponding terrain objects in Blender.
3. If you enabled "Material Creation", the plugin will generate materials based on the textures defined in the JSON files.
4. Once the import is complete, you can save the Blender file to the specified destination folder.

## Troubleshooting

- If no JSON files are found in the folder, ensure the path is correct and the files are generated properly using the Archlord tool.
- If textures are missing, check that they are present in the specified texture folder.

## License

This add-on is licensed under the MIT License. See LICENSE for more details.
