from enum import Enum

class _StrEnum(str, Enum):
    def __str__(self):
        return self.value

class PropertyType(_StrEnum):
    INT = "bpy.props.IntProperty()"
    FLOAT = "bpy.props.FloatProperty()"
    STRING = "bpy.props.StringProperty()"

    @staticmethod
    def get(_type, default: 'PropertyType'):
        if not isinstance(_type, type):
            _type = type(_type)

        if _type == type(int):
            return PropertyType.INT.value
        elif _type == type(float):
            return PropertyType.FLOAT.value
        elif _type == type(str):
            return PropertyType.STRING.value
        else:
            return default.value


class DriverVarType(_StrEnum):
    SINGLE_PROP = "SINGLE_PROP"
    TRANSFORMS = "TRANSFORMS"
    ROTATION_DIFF = "ROTATION_DIFF"
    LOC_DIFF = "LOC_DIFF"
    CONTEXT_PROP = "CONTEXT_PROP"


class DriverVarTransformsTarget(_StrEnum):
    LOC_X = "LOC_X"
    LOC_Y = "LOC_Y"
    LOC_Z = "LOC_Z"
    ROT_X = "ROT_X"
    ROT_Y = "ROT_Y"
    ROT_Z = "ROT_Z"
    SCALE_X = "SCALE_X"
    SCALE_Y = "SCALE_Y"
    SCALE_Z = "SCALE_Z"


class DriverVarTransformsDataPath(_StrEnum):
    LOCATION = "location"
    ROTATION_EULER = "rotation_euler"
    ROTATION_QUATERNION = "rotation_quaternion"
    SCALE = "scale"
    DIMENSIONS = "dimensions"
    BOUND_BOX = "bound_box"


class BlendMode(_StrEnum):
    OPAQUE = "OPAQUE"
    CLIP = "CLIP"
    HASHED = "HASHED"
    BLEND = "BLEND"


class WorkSpaceId(_StrEnum):
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


class SpaceType(_StrEnum):
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


class PropertiesTab(_StrEnum):
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



class KeyCode(_StrEnum):
    NONE = 'NONE'
    LEFTMOUSE = 'LEFTMOUSE'
    MIDDLEMOUSE = 'MIDDLEMOUSE'
    RIGHTMOUSE = 'RIGHTMOUSE'
    BUTTON4MOUSE = 'BUTTON4MOUSE'
    BUTTON5MOUSE = 'BUTTON5MOUSE'
    BUTTON6MOUSE = 'BUTTON6MOUSE'
    BUTTON7MOUSE = 'BUTTON7MOUSE'
    PEN = 'PEN'
    ERASER = 'ERASER'
    MOUSEMOVE = 'MOUSEMOVE'
    INBETWEEN_MOUSEMOVE = 'INBETWEEN_MOUSEMOVE'
    TRACKPADPAN = 'TRACKPADPAN'
    TRACKPADZOOM = 'TRACKPADZOOM'
    MOUSEROTATE = 'MOUSEROTATE'
    MOUSESMARTZOOM = 'MOUSESMARTZOOM'
    WHEELUPMOUSE = 'WHEELUPMOUSE'
    WHEELDOWNMOUSE = 'WHEELDOWNMOUSE'
    WHEELINMOUSE = 'WHEELINMOUSE'
    WHEELOUTMOUSE = 'WHEELOUTMOUSE'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    ZERO = 'ZERO'
    ONE = 'ONE'
    TWO = 'TWO'
    THREE = 'THREE'
    FOUR = 'FOUR'
    FIVE = 'FIVE'
    SIX = 'SIX'
    SEVEN = 'SEVEN'
    EIGHT = 'EIGHT'
    NINE = 'NINE'
    LEFT_CTRL = 'LEFT_CTRL'
    LEFT_ALT = 'LEFT_ALT'
    LEFT_SHIFT = 'LEFT_SHIFT'
    RIGHT_ALT = 'RIGHT_ALT'
    RIGHT_CTRL = 'RIGHT_CTRL'
    RIGHT_SHIFT = 'RIGHT_SHIFT'
    OSKEY = 'OSKEY'
    APP = 'APP'
    GRLESS = 'GRLESS'
    ESC = 'ESC'
    TAB = 'TAB'
    RET = 'RET'
    SPACE = 'SPACE'
    LINE_FEED = 'LINE_FEED'
    BACK_SPACE = 'BACK_SPACE'
    DEL = 'DEL'
    SEMI_COLON = 'SEMI_COLON'
    PERIOD = 'PERIOD'
    COMMA = 'COMMA'
    QUOTE = 'QUOTE'
    ACCENT_GRAVE = 'ACCENT_GRAVE'
    MINUS = 'MINUS'
    PLUS = 'PLUS'
    SLASH = 'SLASH'
    BACK_SLASH = 'BACK_SLASH'
    EQUAL = 'EQUAL'
    LEFT_BRACKET = 'LEFT_BRACKET'
    RIGHT_BRACKET = 'RIGHT_BRACKET'
    LEFT_ARROW = 'LEFT_ARROW'
    DOWN_ARROW = 'DOWN_ARROW'
    RIGHT_ARROW = 'RIGHT_ARROW'
    UP_ARROW = 'UP_ARROW'
    NUMPAD_2 = 'NUMPAD_2'
    NUMPAD_4 = 'NUMPAD_4'
    NUMPAD_6 = 'NUMPAD_6'
    NUMPAD_8 = 'NUMPAD_8'
    NUMPAD_1 = 'NUMPAD_1'
    NUMPAD_3 = 'NUMPAD_3'
    NUMPAD_5 = 'NUMPAD_5'
    NUMPAD_7 = 'NUMPAD_7'
    NUMPAD_9 = 'NUMPAD_9'
    NUMPAD_PERIOD = 'NUMPAD_PERIOD'
    NUMPAD_SLASH = 'NUMPAD_SLASH'
    NUMPAD_ASTERIX = 'NUMPAD_ASTERIX'
    NUMPAD_0 = 'NUMPAD_0'
    NUMPAD_MINUS = 'NUMPAD_MINUS'
    NUMPAD_ENTER = 'NUMPAD_ENTER'
    NUMPAD_PLUS = 'NUMPAD_PLUS'
    F1 = 'F1'
    F2 = 'F2'
    F3 = 'F3'
    F4 = 'F4'
    F5 = 'F5'
    F6 = 'F6'
    F7 = 'F7'
    F8 = 'F8'
    F9 = 'F9'
    F10 = 'F10'
    F11 = 'F11'
    F12 = 'F12'
    F13 = 'F13'
    F14 = 'F14'
    F15 = 'F15'
    F16 = 'F16'
    F17 = 'F17'
    F18 = 'F18'
    F19 = 'F19'
    F20 = 'F20'
    F21 = 'F21'
    F22 = 'F22'
    F23 = 'F23'
    F24 = 'F24'
    PAUSE = 'PAUSE'
    INSERT = 'INSERT'
    HOME = 'HOME'
    PAGE_UP = 'PAGE_UP'
    PAGE_DOWN = 'PAGE_DOWN'
    END = 'END'
    MEDIA_PLAY = 'MEDIA_PLAY'
    MEDIA_STOP = 'MEDIA_STOP'
    MEDIA_FIRST = 'MEDIA_FIRST'
    MEDIA_LAST = 'MEDIA_LAST'
    TEXTINPUT = 'TEXTINPUT'
    WINDOW_DEACTIVATE = 'WINDOW_DEACTIVATE'
    TIMER = 'TIMER'
    TIMER0 = 'TIMER0'
    TIMER1 = 'TIMER1'
    TIMER2 = 'TIMER2'
    TIMER_JOBS = 'TIMER_JOBS'
    TIMER_AUTOSAVE = 'TIMER_AUTOSAVE'
    TIMER_REPORT = 'TIMER_REPORT'
    TIMERREGION = 'TIMERREGION'
    NDOF_MOTION = 'NDOF_MOTION'
    NDOF_BUTTON_MENU = 'NDOF_BUTTON_MENU'
    NDOF_BUTTON_FIT = 'NDOF_BUTTON_FIT'
    NDOF_BUTTON_TOP = 'NDOF_BUTTON_TOP'
    NDOF_BUTTON_BOTTOM = 'NDOF_BUTTON_BOTTOM'
    NDOF_BUTTON_LEFT = 'NDOF_BUTTON_LEFT'
    NDOF_BUTTON_RIGHT = 'NDOF_BUTTON_RIGHT'
    NDOF_BUTTON_FRONT = 'NDOF_BUTTON_FRONT'
    NDOF_BUTTON_BACK = 'NDOF_BUTTON_BACK'
    NDOF_BUTTON_ISO1 = 'NDOF_BUTTON_ISO1'
    NDOF_BUTTON_ISO2 = 'NDOF_BUTTON_ISO2'
    NDOF_BUTTON_ROLL_CW = 'NDOF_BUTTON_ROLL_CW'
    NDOF_BUTTON_ROLL_CCW = 'NDOF_BUTTON_ROLL_CCW'
    NDOF_BUTTON_SPIN_CW = 'NDOF_BUTTON_SPIN_CW'
    NDOF_BUTTON_SPIN_CCW = 'NDOF_BUTTON_SPIN_CCW'
    NDOF_BUTTON_TILT_CW = 'NDOF_BUTTON_TILT_CW'
    NDOF_BUTTON_TILT_CCW = 'NDOF_BUTTON_TILT_CCW'
    NDOF_BUTTON_ROTATE = 'NDOF_BUTTON_ROTATE'
    NDOF_BUTTON_PANZOOM = 'NDOF_BUTTON_PANZOOM'
    NDOF_BUTTON_DOMINANT = 'NDOF_BUTTON_DOMINANT'
    NDOF_BUTTON_PLUS = 'NDOF_BUTTON_PLUS'
    NDOF_BUTTON_MINUS = 'NDOF_BUTTON_MINUS'
    NDOF_BUTTON_V1 = 'NDOF_BUTTON_V1'
    NDOF_BUTTON_V2 = 'NDOF_BUTTON_V2'
    NDOF_BUTTON_V3 = 'NDOF_BUTTON_V3'
    NDOF_BUTTON_1 = 'NDOF_BUTTON_1'
    NDOF_BUTTON_2 = 'NDOF_BUTTON_2'
    NDOF_BUTTON_3 = 'NDOF_BUTTON_3'
    NDOF_BUTTON_4 = 'NDOF_BUTTON_4'
    NDOF_BUTTON_5 = 'NDOF_BUTTON_5'
    NDOF_BUTTON_6 = 'NDOF_BUTTON_6'
    NDOF_BUTTON_7 = 'NDOF_BUTTON_7'
    NDOF_BUTTON_8 = 'NDOF_BUTTON_8'
    NDOF_BUTTON_9 = 'NDOF_BUTTON_9'
    NDOF_BUTTON_10 = 'NDOF_BUTTON_10'
    NDOF_BUTTON_A = 'NDOF_BUTTON_A'
    NDOF_BUTTON_B = 'NDOF_BUTTON_B'
    NDOF_BUTTON_C = 'NDOF_BUTTON_C'
    ACTIONZONE_AREA = 'ACTIONZONE_AREA'
    ACTIONZONE_REGION = 'ACTIONZONE_REGION'
    ACTIONZONE_FULLSCREEN = 'ACTIONZONE_FULLSCREEN'
    XR_ACTION = 'XR_ACTION'
