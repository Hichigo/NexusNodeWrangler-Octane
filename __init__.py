bl_info = {
    "name": "Nexus Node Wrangler Octane",
    "author": "Nexus Studio",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "Node Editor > alt-shift-T key",
    "description": "",
    "wiki_url": "none",
    "category": "Node",
}

import bpy
from bpy.types import Operator, Panel
from bpy.props import (
    FloatProperty,
    EnumProperty,
    BoolProperty,
    IntProperty,
    StringProperty,
    FloatVectorProperty,
    CollectionProperty,
)

from bpy_extras.io_utils import ImportHelper

def check_space(context):
    space = context.space_data
    valid_trees = ["ShaderNodeTree", "CompositorNodeTree", "TextureNodeTree"]

    return (space.type == 'NODE_EDITOR' and space.node_tree is not None and space.tree_type in valid_trees)

class NWBase:
    @classmethod
    def poll(cls, context):
        return check_space(context)

class NWAddOctaneSetup(Operator, NWBase, ImportHelper):
    bl_idname = "node.nw_add_textures_for_octane"
    bl_label = "Octane Texture Setup"
    bl_description = "Add Texture Node Setup for Octane"
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
        pass
        return {'FINISHED'}


addon_keymaps = []
kmi_defs = (
    (NWAddOctaneSetup.bl_idname, 'T', 'PRESS', True, True, False, None, "Add Principled texture setup"),
)

classes = (
    NWAddOctaneSetup,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        for (identifier, key, action, CTRL, SHIFT, ALT, props, nicename) in kmi_defs:
            kmi = km.keymap_items.new(identifier, key, action, ctrl=CTRL, shift=SHIFT, alt=ALT)
            addon_keymaps.append((km, kmi))

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
