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
from ..utils import get_addon_prefs

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
        if not (active_node and active_node.bl_idname == 'ShaderNodeBsdfPrincipled'):
            self.report({'INFO'}, 'Select Principled BSDF')
            return {'CANCELLED'}

        addon_prefs = get_addon_prefs(context)


        return {'FINISHED'}

    def get_nodes_links(self, context):
        tree = context.space_data.node_tree

        if tree.nodes.active:
            while tree.nodes.active != context.active_node:
                tree = tree.nodes.active.node_tree

        return tree.nodes, tree.links
