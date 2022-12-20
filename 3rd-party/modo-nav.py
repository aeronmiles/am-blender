import bpy
x = bpy.context.preferences

"""
Make 3D View navigation compatible with MODO:

    To rotate press the alt/option key alone and LMB-click drag over the viewport

    Zoom by holding ctrl/command + alt/option and LMB-click dragging over the viewport

    Pressing both the shift and alt/option keys and then LMB-click dragging over
    the viewport will move the view position around left and right and up and down
"""
#x.view.use_mouse_depth_navigate = True # enable: Auto Depth
#x.view.use_zoom_to_mouse = True # enable: Zoom To Mouse Position
x.inputs.use_mouse_emulate_3_button = False # enable: Emulate 3 Button Mouse
x.inputs.view_rotate_method = 'TURNTABLE' #'TRACKBALL' # Orbit Style: Trackball
x.inputs.view_zoom_axis = 'HORIZONTAL' # Zoom Style: Horizontal
x.inputs.view_rotate_sensitivity_turntable = 0.00698132 * 1.1

"""
optional, non-default, but recommended settings:
"""
#x.view.use_auto_perspective = True # enable: Auto Perspective (auto orthographic views)
x.system.use_region_overlap = True # enable: Region Overlap (makes Tool Shelf transparent)

"""
save all settings as default:
"""
#bpy.ops.wm.save_userpref()
