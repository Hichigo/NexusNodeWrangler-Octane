import bpy

def get_separators():
    addon_prefs = get_addon_prefs()
    separators = addon_prefs.separators
    return separators.split(',')

def get_node_inputs_with_tags():
    addon_prefs = get_addon_prefs()
    tags = addon_prefs.ocatane_textures_tags

    node_inputs_with_tags = {
        'Transmission': {
            'name_to_connect_input': 'Transmission',
            'tags': tags.transmission.split(' '),
            'img_path': '',
            'node': ''
        },
        'Albedo color': {
            'name_to_connect_input': 'Albedo color',
            'tags': tags.albedo_color.split(' '),
            'img_path': '',
            'node': ''
        },
        'Ambient occlusion': {
            'name_to_connect_input': 'Albedo color',
            'tags': tags.ambient_occlusion.split(' '),
            'img_path': '',
            'node': ''
        },
        'Metallic': {
            'name_to_connect_input': 'Metallic',
            'tags': tags.metallic.split(' '),
            'img_path': '',
            'node': ''
        },
        'Specular': {
            'name_to_connect_input': 'Specular',
            'tags': tags.specular.split(' '),
            'img_path': '',
            'node': ''
        },
        'Roughness': {
            'name_to_connect_input': 'Roughness',
            'tags': tags.roughness.split(' '),
            'img_path': '',
            'node': ''
        },
        'Gloss': {
            'name_to_connect_input': 'Roughness',
            'tags': tags.gloss.split(' '),
            'img_path': '',
            'node': ''
        },
        'Opacity': {
            'name_to_connect_input': 'Opacity',
            'tags': tags.opacity.split(' '),
            'img_path': '',
            'node': ''
        },
        'Bump': {
            'name_to_connect_input': 'Bump',
            'tags': tags.bump.split(' '),
            'img_path': '',
            'node': ''
        },
        'Normal': {
            'name_to_connect_input': 'Normal',
            'tags': tags.normal.split(' '),
            'img_path': '',
            'node': ''
        },
        'Displacement': {
            'name_to_connect_input': 'Displacement',
            'tags': tags.displacement.split(' '),
            'img_path': '',
            'node': ''
        }
    }

    return node_inputs_with_tags


def get_addon_prefs():
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[get_addon_name()].preferences

    return addon_prefs

def get_addon_name():
    return __name__.split('.')[0]
