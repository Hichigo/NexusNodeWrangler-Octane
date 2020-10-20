import bpy
from os import path
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
from ..utils import get_separators, get_node_inputs_with_tags


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
        """ main algorithm import textures, create nodes and links nodes """
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

        # new_texture_nodes = []
        for texture_file in self.files:
            # texture_node = nodes.new(type="ShaderNodeOctFloatImageTex")
            texture_path = path.join(self.directory, texture_file.name)
            texture_name_parts = path.splitext(texture_file.name)[0]

            texture_name_parts = self.split_texture_name(texture_name=texture_name_parts)

            if path.isfile(texture_path):
                self.set_texture_type_by_tag(
                    node_inputs_with_tags=node_inputs_with_tags,
                    texture_name_parts=texture_name_parts,
                    texture_path=texture_path
                )

        print(node_inputs_with_tags)



                # img = bpy.data.images.load(path.join(self.directory, texture_file.name))
                # texture_node.image = img
                # new_texture_nodes.append(texture_node)

        # old_node = new_texture_nodes[0]
        # old_node.location = Vector((active_node.location.x-500, active_node.location.y+1000))
        # for node in new_texture_nodes:
        #     node.location = old_node.location - Vector((0, 300))

        #     old_node = node

        # TODO: create links
        # link = links.new(active_node.inputs["Albedo color"], new_texture_nodes[0].outputs[0])

        return {'FINISHED'}

    def get_nodes_links(self, context):
        """ returned nodes and links """
        tree = context.space_data.node_tree

        if tree.nodes.active:
            while tree.nodes.active != context.active_node:
                tree = tree.nodes.active.node_tree

        return tree.nodes, tree.links

    def split_texture_name(self, texture_name):
        """ split texture name by separators """
        seperators = get_separators()
        for sep in seperators:
            texture_name = texture_name.replace(sep, ' ')
        texture_name = texture_name.lower()
        return texture_name

    def set_texture_type_by_tag(self, node_inputs_with_tags, texture_name_parts, texture_path):
        """ find by tag input object and remember texture path """
        for input_name, input_obj in node_inputs_with_tags.items():
            for tag in input_obj['tags']:
                tag = tag.lower()
                if tag in texture_name_parts:
                    input_obj['img_path'] = texture_path
                    return
