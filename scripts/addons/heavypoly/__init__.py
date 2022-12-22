from . import HEAVYPOLY__menu_master
from . import HEAVYPOLY_draw_primitives
from . import HEAVYPOLY_HOTKEYS
from . import HEAVYPOLY_OPERATORS
from . import HEAVYPOLY_panel_properties
from . import HEAVYPOLY_panel_render
from . import HEAVYPOLY_pie_add
from . import HEAVYPOLY_pie_areas
from . import HEAVYPOLY_pie_boolean
from . import HEAVYPOLY_pie_import_export
from . import HEAVYPOLY_pie_pivots
from . import HEAVYPOLY_pie_rotate_90
from . import HEAVYPOLY_pie_save
from . import HEAVYPOLY_pie_selection
from . import HEAVYPOLY_pie_shading
from . import HEAVYPOLY_pie_specials
from . import HEAVYPOLY_pie_symmetry
from . import HEAVYPOLY_pie_view
from . import HEAVYPOLY_popup_materials
from . import HEAVYPOLY_popup_properties
from . import HEAVYPOLY_popup_render
from . import HEAVYPOLY_select_through_border
from . import jmQuickPipe

from bpy.app.handlers import persistent

bl_info = {
    "name": "Heavypoly",
    "description": "",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "3D"
}


def register():
    HEAVYPOLY__menu_master.register()
    HEAVYPOLY_draw_primitives.register()
    HEAVYPOLY_HOTKEYS.register()
    HEAVYPOLY_OPERATORS.register()
    HEAVYPOLY_panel_properties.register()
    HEAVYPOLY_panel_render.register()
    HEAVYPOLY_pie_add.register()
    HEAVYPOLY_pie_areas.register()
    HEAVYPOLY_pie_boolean.register()
    HEAVYPOLY_pie_import_export.register()
    HEAVYPOLY_pie_pivots.register()
    HEAVYPOLY_pie_rotate_90.register()
    HEAVYPOLY_pie_save.register()
    HEAVYPOLY_pie_selection.register()
    HEAVYPOLY_pie_shading.register()
    HEAVYPOLY_pie_specials.register()
    HEAVYPOLY_pie_symmetry.register()
    HEAVYPOLY_pie_view.register()
    HEAVYPOLY_popup_materials.register()
    HEAVYPOLY_popup_properties.register()
    HEAVYPOLY_popup_render.register()
    HEAVYPOLY_select_through_border.register()
    jmQuickPipe.register()


def unregister():
    HEAVYPOLY__menu_master.unregister()
    HEAVYPOLY_draw_primitives.unregister()
    HEAVYPOLY_HOTKEYS.unregister()
    HEAVYPOLY_OPERATORS.unregister()
    HEAVYPOLY_panel_properties.unregister()
    HEAVYPOLY_panel_render.unregister()
    HEAVYPOLY_pie_add.unregister()
    HEAVYPOLY_pie_areas.unregister()
    HEAVYPOLY_pie_boolean.unregister()
    HEAVYPOLY_pie_import_export.unregister()
    HEAVYPOLY_pie_pivots.unregister()
    HEAVYPOLY_pie_rotate_90.unregister()
    HEAVYPOLY_pie_save.unregister()
    HEAVYPOLY_pie_selection.unregister()
    HEAVYPOLY_pie_shading.unregister()
    HEAVYPOLY_pie_specials.unregister()
    HEAVYPOLY_pie_symmetry.unregister()
    HEAVYPOLY_pie_view.unregister()
    HEAVYPOLY_popup_materials.unregister()
    HEAVYPOLY_popup_properties.unregister()
    HEAVYPOLY_popup_render.unregister()
    HEAVYPOLY_select_through_border.unregister()
    jmQuickPipe.unregister()