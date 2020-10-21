import bpy

def get_separators():
    addon_prefs = get_addon_prefs()
    separators = addon_prefs.separators
    return separators.split(",")

def get_node_inputs_with_tags():
    addon_prefs = get_addon_prefs()
    tags = addon_prefs.ocatane_textures_tags

    node_inputs_with_tags = {
        "Transmission": {
            "tags": tags.transmission.split(' '),
            "img_path": '',
            "node": ''
        },
        "Albedo color": {
            "tags": tags.albedo_color.split(' '),
            "img_path": '',
            "node": ''
        },
        "Ambient occlusion": {
            "tags": tags.ambient_occlusion.split(' '),
            "img_path": '',
            "node": ''
        },
        "Metallic": {
            "tags": tags.metallic.split(' '),
            "img_path": '',
            "node": ''
        },
        "Specular": {
            "tags": tags.specular.split(' '),
            "img_path": '',
            "node": ''
        },
        "Roughness": {
            "tags": tags.roughness.split(' '),
            "img_path": '',
            "node": ''
        },
        "Gloss": {
            "tags": tags.gloss.split(' '),
            "img_path": '',
            "node": ''
        },
        "Opacity": {
            "tags": tags.opacity.split(' '),
            "img_path": '',
            "node": ''
        },
        "Bump": {
            "tags": tags.bump.split(' '),
            "img_path": '',
            "node": ''
        },
        "Normal": {
            "tags": tags.normal.split(' '),
            "img_path": '',
            "node": ''
        },
        "Displacement": {
            "tags": tags.displacement.split(' '),
            "img_path": '',
            "node": ''
        }
    }

    return node_inputs_with_tags


def get_addon_prefs():
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[get_addon_name()].preferences

    return addon_prefs

def get_addon_name():
    return __name__.split(".")[0]
