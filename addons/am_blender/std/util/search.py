
from bpy.props import StringProperty, BoolProperty, EnumProperty
import bpy
from bpy.props import *
import rna_keymap_ui
from ...std import log

bl_info = {
    "name": "Viewport Search",
    "author": "Amandeep",
    "description": "Search and Select Objects from directly from the viewport viewport",
    "blender": (3, 1, 0),
    "version": (1, 0, 0),
    "warning": "",
    "category": "3D View",
}


def preferences():
    return bpy.context.preferences.addons[__package__].preferences


def draw_hotkeys(col, km_name):
    kc = bpy.context.window_manager.keyconfigs.user
    for kmi in [a.idname for b, a in addon_keymaps]:
        km2 = kc.keymaps[km_name]
        kmi2 = []
        for a, b in km2.keymap_items.items():
            if a == kmi:
                kmi2.append(b)
        if kmi2:
            for a in kmi2:
                col.context_pointer_set("keymap", km2)
                rna_keymap_ui.draw_kmi([], kc, km2, a, col, 0)


def add_to_existing_menu(draw_func, name, prepend=False):
    try:
        if not getattr(bpy.types, name).is_extended() or draw_func not in getattr(bpy.types, name).draw._draw_funcs[:]:
            if prepend:
                getattr(bpy.types, name).prepend(draw_func)
            else:
                getattr(bpy.types, name).append(draw_func)
    except Exception as e:
        log.error("Could not add the draw function!", e)


def remove_from_menu(draw_func, name):
    try:
        if getattr(bpy.types, name).is_extended() and draw_func in getattr(bpy.types, name).draw._draw_funcs[:]:
            getattr(bpy.types, name).remove(draw_func)
    except Exception as e:
        log.error("Could not remove the draw function!", e)


icon_map = {'MESH': 'MESH',
            'CAMERA': 'CAMERA',
            'CURVE': 'CURVE',

            'SURFACE': 'SURFACE',

            'META': 'META',

            'FONT': 'FONT',

            'CURVES': 'CURVE',

            'POINTCLOUD': 'POINTCLOUD',

            'VOLUME': 'VOLUME',

            'GPENCIL': 'GREASEPENCIL',

            'ARMATURE': 'ARMATURE',

            'LATTICE': 'LATTICE',

            'EMPTY': 'EMPTY',

            'LIGHT': 'LIGHT',

            'LIGHT_PROBE': 'LIGHTPROBE',

            'SPEAKER': 'SPEAKER'}


def select(obj, active=True):

    if obj:
        obj.select_set(True)
        if active:
            bpy.context.view_layer.objects.active = obj


def get_objects(self, context):
    return [(a.name, a.name, a.name, f"OUTLINER_OB_{icon_map[a.type.upper()]}", i) for i, a in enumerate(context.scene.objects)]


class VSPrefs(bpy.types.AddonPreferences, AddonUpdateChecker):
    bl_idname = __package__
    auto_highlight_in_outliner: bpy.props.BoolProperty(
        default=True, name='Auto Highlight in Outliner')
    show_search_button: bpy.props.BoolProperty(
        default=False, name='Show Search button in header')

    def draw(self, context):
        layout = self.layout
        draw_update_section_for_prefs(layout)
        draw_hotkeys(layout, "3D View")
        layout.prop(self, 'auto_highlight_in_outliner')
        layout.prop(self, 'show_search_button')


enum_items = [("None", "None", "None"), ]


def get_searchable_items(self, context):

    global enum_items
    return enum_items


class VS_OT_Search_And_Select(bpy.types.Operator):
    bl_idname = "vs.search"
    bl_label = "Viewport Search"
    bl_property = "my_enum"
    my_enum: bpy.props.EnumProperty(
        name="Panel", description="", items=get_searchable_items)

    def execute(self, context):
        for obj in context.view_layer.objects:
            try:
                if obj.name == self.my_enum:
                    select(obj, True)
                else:
                    obj.select_set(False)
            except Exception as e:
                log.error(e)
        bpy.ops.view3d.view_selected('INVOKE_DEFAULT')
        if preferences().auto_highlight_in_outliner:
            override = None
            for area in context.screen.areas:
                if 'OUTLINER' in area.type:
                    for region in area.regions:
                        if 'WINDOW' in region.type:
                            override = {'area': area, 'region': region}
                            break
                    break
            if override is not None:
                bpy.ops.outliner.show_active(override)

        return {'FINISHED'}

    def invoke(self, context, event):
        global enum_items
        enum_items = [(a.name, a.name, a.name, f"OUTLINER_OB_{icon_map[a.type.upper()]}", i) for i, a in enumerate(
            context.view_layer.objects) if a.visible_get()]
        wm = context.window_manager

        wm.invoke_search_popup(self)
        return {'FINISHED'}


# Only needed if you want to add into a dynamic menu
def add_to_header(self, context):
    if preferences().show_search_button:
        self.layout.operator(
            VS_OT_Search_And_Select.bl_idname, icon='VIEWZOOM')


classes = (VS_OT_Search_And_Select, VSPrefs
           )

icon_collection = {}
addon_keymaps = []


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    kmaps = [("vs.search", 'F', 'ctrl'),
             ]

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    if kc:
        for (op, k, sp) in kmaps:

            kmi = km.keymap_items.new(
                op,
                type=k,
                value="PRESS",
                alt="alt" in sp,
                shift="shift" in sp,
                ctrl="ctrl" in sp,
            )
            addon_keymaps.append((km, kmi))
    add_to_existing_menu(add_to_header, "VIEW3D_HT_tool_header")


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
    for (km, kmi) in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    remove_from_menu(add_to_header, "VIEW3D_HT_tool_header")
