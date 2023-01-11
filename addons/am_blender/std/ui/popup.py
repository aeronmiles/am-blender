from ...std import *
from loguru import logger
import bpy

# TODO: fix this
@logger.catch
def MessagePopup(message="", title="Message Box", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)
