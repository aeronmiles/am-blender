from enum import Enum


class BlendMode(Enum):
    OPAQUE = "OPAQUE"
    CLIP = "CLIP"
    HASHED = "HASHED"
    BLEND = "BLEND"


class WorkSpaceId(Enum):
    Modeling = "Modeling"
    UVEditing = "UV Editing"
    Layout = "Layout"
    Sculpting = "Sculpting"
    TexturePaint = "Texture Paint"
    Shading = "Shading"
    Rendering = "Rendering"
    Compositing = "Compositing"
    GeometryNodes = "Geometry Nodes"
    Scripting = "Scripting"
    Assets = "Assets"


class SpaceType(Enum):
    EMPTY = ''
    VIEW_3D = 'VIEW_3D'
    IMAGE_EDITOR = 'IMAGE_EDITOR'
    NODE_EDITOR = 'NODE_EDITOR'
    SEQUENCE_EDITOR = 'SEQUENCE_EDITOR'
    CLIP_EDITOR = 'CLIP_EDITOR'
    DOPESHEET_EDITOR = 'DOPESHEET_EDITOR'
    GRAPH_EDITOR = 'GRAPH_EDITOR'
    NLA_EDITOR = 'NLA_EDITOR'
    TEXT_EDITOR = 'TEXT_EDITOR'
    CONSOLE = 'CONSOLE'
    INFO = 'INFO'
    TOP_BAR = 'TOP_BAR'
    STATUS_BAR = 'STATUS_BAR'
    OUTLINER = 'OUTLINER'
    PROPERTIES = 'PROPERTIES'
    FILE_BROWSER = 'FILE_BROWSER'
    SPREADSHEET = 'SPREADSHEET'
    PREFERENCES = 'PREFERENCES'
