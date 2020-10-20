import bpy
from bpy.props import (
    FloatProperty,
    EnumProperty,
    BoolProperty,
    IntProperty,
    StringProperty,
    FloatVectorProperty,
    CollectionProperty,
)
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper
from mathutils import Vector
from os import path
from ..utils import get_node_inputs_with_tags

def check_space(context):
    space = context.space_data
    valid_trees = ["ShaderNodeTree", "CompositorNodeTree", "TextureNodeTree"]

    return (space.type == 'NODE_EDITOR' and space.node_tree is not None and space.tree_type in valid_trees)

class NWBase:
    @classmethod
    def poll(cls, context):
        return check_space(context)

class NWAddOctaneTextures(Operator, NWBase, ImportHelper):
    bl_idname = "node.nw_add_textures_for_octane"
    bl_label = "Add Octane Textures"
    bl_description = "Add Textures Node Setup for Octane"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(
        name='Directory',
        subtype='DIR_PATH',
        default='',
        description='Folder to search in for image files'
    )
    files: CollectionProperty(
        type=bpy.types.OperatorFileListElement,
        options={'HIDDEN', 'SKIP_SAVE'}
    )
    relative_path: BoolProperty(
        name='Relative Path',
        description='Select the file relative to the blend file',
        default=True
    )
    order = [
        "filepath",
        "files",
    ]

    def draw(self, context):
        layout = self.layout
        layout.alignment = 'LEFT'

        layout.prop(self, 'relative_path')

    @classmethod
    def poll(cls, context):
        return check_space(context)

    def execute(self, context):
        if not self.directory:
            self.report({'INFO'}, 'No Folder Selected')
            return {'CANCELLED'}

        if not self.files[:]:
            self.report({'INFO'}, 'No Files Selected')
            return {'CANCELLED'}

        nodes, links = self.get_nodes_links(context)
        active_node = nodes.active
        if not (active_node and active_node.bl_idname == 'ShaderNodeOctUniversalMat'):
            self.report({'INFO'}, 'Select Universal Octane material')
            return {'CANCELLED'}

        node_inputs_with_tags = get_node_inputs_with_tags()

        # TODO: tags
        for input_name, input in node_inputs_with_tags.items():
            print(input_name, input)

        new_texture_nodes = []
        for texture_file in self.files:
            texture_node = nodes.new(type="ShaderNodeOctFloatImageTex")
            if texture_file.name != '':
                img = bpy.data.images.load(path.join(self.directory, texture_file.name))
                texture_node.image = img
                new_texture_nodes.append(texture_node)

        old_node = new_texture_nodes[0]
        old_node.location = Vector((active_node.location.x-500, active_node.location.y+1000))
        for node in new_texture_nodes:
            node.location = old_node.location - Vector((0, 300))

            old_node = node

        # TODO: create links
        link = links.new(active_node.inputs["Albedo color"], new_texture_nodes[0].outputs[0])

        return {'FINISHED'}

    def get_nodes_links(self, context):
        tree = context.space_data.node_tree

        if tree.nodes.active:
            while tree.nodes.active != context.active_node:
                tree = tree.nodes.active.node_tree

        return tree.nodes, tree.links
