from enum import Enum


class DriverVarType(Enum):
    SINGLE_PROP = "SINGLE_PROP"
    TRANSFORMS = "TRANSFORMS"
    ROTATION_DIFF = "ROTATION_DIFF"
    LOC_DIFF = "LOC_DIFF"
    CONTEXT_PROP = "CONTEXT_PROP"


class DriverVarTransformsTarget(Enum):
    LOC_X = "LOC_X"
    LOC_Y = "LOC_Y"
    LOC_Z = "LOC_Z"
    ROT_X = "ROT_X"
    ROT_Y = "ROT_Y"
    ROT_Z = "ROT_Z"
    SCALE_X = "SCALE_X"
    SCALE_Y = "SCALE_Y"
    SCALE_Z = "SCALE_Z"


class DriverVarTransformsDataPath(Enum):
    LOCATION = "location"
    ROTATION_EULER = "rotation_euler"
    ROTATION_QUATERNION = "rotation_quaternion"
    SCALE = "scale"
    DIMENSIONS = "dimensions"
    BOUND_BOX = "bound_box"


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


class PropertiesTab(Enum):
    TOOL = 'TOOL'
    RENDER = "RENDER"
    OUTPUT = "OUTPUT"
    VIEW_LAYER = "VIEW_LAYER"
    SCENE = "SCENE"
    WORLD = "WORLD"
    COLLECTION = "COLLECTION"
    OBJECT = "OBJECT"
    MODIFIER = "MODIFIER"
    PARTICLES = "PARTICLES"
    PHYSICS = "PHYSICS"
    CONSTRAINT = "CONSTRAINT"
    DATA = "DATA"  # This corresponds to the mesh tab
    MATERIAL = "MATERIAL"
    TEXTURE = "TEXTURE"
