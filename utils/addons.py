import bpy

def addon_exists(name):
    for addon_name in bpy.context.user_preferences.addons.keys():
        if name in addon_name: return True
    return False