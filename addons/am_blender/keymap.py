import bpy


def keymaps():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new('Window', space_type='EMPTY',
                                         region_type='WINDOW', modal=False)

    km.keymap_items.new(
        "wm.call_menu_pie", "C", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ConvertPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "P", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_CustomPropPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "Z", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ShaderUtilPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "X", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ObjectPropertiesPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "E", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_DataUtilPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "B", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_BuildPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "S", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ImportExportPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "W", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_Nav_Workspace_Pie"

    km.keymap_items.new(
        "wm.call_menu_pie", "Q", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_Nav_Properties_Tab"

    km.keymap_items.new(
        "wm.call_menu_pie", "A", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ModifiersPie"

    km.keymap_items.new(
        "wm.call_menu_pie", "\\", "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ViewPie"

def register():
    keymaps()


def unregister():
    pass
