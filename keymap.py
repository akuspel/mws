import bpy


"""addon_keymaps = []


def register_keymap():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    # register to 3d view mode tab
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")

    #kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", shift=True)
    #kmi.properties.name = "hops_main_pie"
    #addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", shift=True, alt=True).properties.name = "pie.mwse"
    kmi.properties.name = "pie.mwse"
    addon_keymaps.append((km, kmi))
    
    kmi = km.keymap_items.new("mesh.quickdelete", "X", "PRESS")
    addon_keymaps.append((km, kmi))

    #kmi = km.keymap_items.new("view3d.hops_helper_popup", "ACCENT_GRAVE", "PRESS", ctrl=True)
    #kmi.properties.tab = "MODIFIERS"
    #addon_keymaps.append((km, kmi))


def unregister_keymap():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()"""

addon_keymaps = []

def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon
    km = addon.keymaps.new(name = "3D View", space_type = "VIEW_3D")
    
    kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", shift=True, alt=True).properties.name = "mwse_pie"
    kmi = km.keymap_items.new("mesh.quickdelete", "X", "PRESS")
    kmi = km.keymap_items.new("mesh.quickmerge", "M", "PRESS", alt=True)
    
    addon_keymaps.append(km)

def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

register_keymaps()