def get_addon_prefs(context):
    preferences = context.preferences
    addon_prefs = preferences.addons[get_addon_name()].preferences

    return addon_prefs

def get_addon_name():
    return __name__.split(".")[0]