import bpy

def get_node_inputs_with_tags():
    addon_prefs = get_addon_prefs()
    tags = addon_prefs.ocatane_textures_tags

    node_inputs_with_tags = {
        "Displacement": {
            "tags": tags.displacement.split(' ')
        },
        "Base Color": {
            "tags": tags.base_color.split(' ')
        },
        "Subsurface Color": {
            "tags": tags.sss_color.split(' ')
        },
        "Metallic": {
            "tags": tags.metallic.split(' ')
        },
        "Specular": {
            "tags": tags.specular.split(' ')
        },
        "Roughness": {
            "tags": tags.rough.split(' ')
        },
        "Normal": {
            "tags": tags.normal.split(' ')
        }
    }

    return node_inputs_with_tags


def get_addon_prefs():
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[get_addon_name()].preferences

    return addon_prefs

def get_addon_name():
    return __name__.split(".")[0]
