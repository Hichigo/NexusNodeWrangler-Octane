bl_info = {
    "name": "Nexus Node Wrangler Octane",
    "author": "Nexus Studio",
    "version": (0, 0, 1),
    "blender": (2, 83, 0),
    "location": "Node Editor > alt-shift-T key",
    "description": "",
    "wiki_url": "none",
    "category": "Node",
}


import bpy
from bpy.types import Operator, Panel
from .AddOctaneTextures.add_octane_textures_op import *

addon_keymaps = []
kmi_defs = (
    (NWAddOctaneTextures.bl_idname, 'T', 'PRESS', True, True, False, None, "Add Principled texture setup"),
)

classes = (
    NWAddOctaneTextures,
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
