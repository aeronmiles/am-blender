from .std.types import KeyCode
import bpy

def keymaps():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new('Window', space_type='EMPTY',
                                         region_type='WINDOW', modal=False)

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.C, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ConvertPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.P, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_CustomPropPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.Z, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ShaderUtilPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.X, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ObjectPropertiesPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.E, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_DataUtilPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.B, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_BuildPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.S, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ImportExportPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.W, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_Nav_Workspace_Pie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.Q, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_Nav_Properties_Tab"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.A, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ModifiersPie"

    km.keymap_items.new(
        "wm.call_menu_pie", KeyCode.ONE, "PRESS", ctrl=True, alt=True, shift=True).properties.name = "AM_MT_ViewPie"

def register():
    keymaps()


def unregister():
    pass

