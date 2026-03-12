"""Key constants mirroring Bubble Tea v2 key codes."""

# Arrow / Navigation
KEY_UP = "up"
KEY_DOWN = "down"
KEY_RIGHT = "right"
KEY_LEFT = "left"
KEY_BEGIN = "begin"
KEY_FIND = "find"
KEY_INSERT = "insert"
KEY_DELETE = "delete"
KEY_SELECT = "select"
KEY_PG_UP = "pgup"
KEY_PG_DOWN = "pgdown"
KEY_HOME = "home"
KEY_END = "end"

# Whitespace / Control
KEY_BACKSPACE = "backspace"
KEY_TAB = "tab"
KEY_ENTER = "enter"
KEY_RETURN = KEY_ENTER
KEY_ESCAPE = "escape"
KEY_ESC = KEY_ESCAPE
KEY_SPACE = "space"

# Lock keys
KEY_CAPS_LOCK = "capslock"
KEY_SCROLL_LOCK = "scrolllock"
KEY_NUM_LOCK = "numlock"
KEY_PRINT_SCREEN = "printscreen"
KEY_PAUSE = "pause"
KEY_MENU = "menu"

# Function keys
_FUNC_KEYS = {i: f"f{i}" for i in range(1, 64)}
KEY_F1, KEY_F2, KEY_F3, KEY_F4, KEY_F5 = (
    _FUNC_KEYS[1], _FUNC_KEYS[2], _FUNC_KEYS[3], _FUNC_KEYS[4], _FUNC_KEYS[5],
)
KEY_F6, KEY_F7, KEY_F8, KEY_F9, KEY_F10 = (
    _FUNC_KEYS[6], _FUNC_KEYS[7], _FUNC_KEYS[8], _FUNC_KEYS[9], _FUNC_KEYS[10],
)
KEY_F11, KEY_F12 = _FUNC_KEYS[11], _FUNC_KEYS[12]
KEY_F13, KEY_F14, KEY_F15, KEY_F16, KEY_F17, KEY_F18, KEY_F19, KEY_F20 = (
    _FUNC_KEYS[i] for i in range(13, 21)
)
KEY_F63 = _FUNC_KEYS[63]

# Keypad
KEY_KP_ENTER = "kpenter"
KEY_KP_EQUAL = "kpequal"
KEY_KP_MULTIPLY = "kpmultiply"
KEY_KP_PLUS = "kpplus"
KEY_KP_COMMA = "kpcomma"
KEY_KP_MINUS = "kpminus"
KEY_KP_DECIMAL = "kpdecimal"
KEY_KP_DIVIDE = "kpdivide"
KEY_KP_0, KEY_KP_1, KEY_KP_2, KEY_KP_3, KEY_KP_4 = (
    f"kp{i}" for i in range(5)
)
KEY_KP_5, KEY_KP_6, KEY_KP_7, KEY_KP_8, KEY_KP_9 = (
    f"kp{i}" for i in range(5, 10)
)
KEY_KP_SEP = "kpsep"
KEY_KP_UP = "kpup"
KEY_KP_DOWN = "kpdown"
KEY_KP_LEFT = "kpleft"
KEY_KP_RIGHT = "kpright"
KEY_KP_PG_UP = "kppgup"
KEY_KP_PG_DOWN = "kppgdown"
KEY_KP_HOME = "kphome"
KEY_KP_END = "kpend"
KEY_KP_INSERT = "kpinsert"
KEY_KP_DELETE = "kpdelete"
KEY_KP_BEGIN = "kpbegin"

# Media keys
KEY_MEDIA_PLAY = "mediaplay"
KEY_MEDIA_PAUSE = "mediapause"
KEY_MEDIA_PLAY_PAUSE = "mediaplaypause"
KEY_MEDIA_REVERSE = "mediareverse"
KEY_MEDIA_STOP = "mediastop"
KEY_MEDIA_FAST_FORWARD = "mediafastforward"
KEY_MEDIA_REWIND = "mediarewind"
KEY_MEDIA_NEXT = "medianext"
KEY_MEDIA_PREV = "mediaprev"
KEY_MEDIA_RECORD = "mediarecord"

# Volume keys
KEY_LOWER_VOL = "lowervol"
KEY_RAISE_VOL = "raisevol"
KEY_MUTE = "mute"

# Modifier keys (as key codes, not modifiers)
KEY_LEFT_SHIFT = "leftshift"
KEY_LEFT_ALT = "leftalt"
KEY_LEFT_CTRL = "leftctrl"
KEY_LEFT_SUPER = "leftsuper"
KEY_LEFT_HYPER = "lefthyper"
KEY_LEFT_META = "leftmeta"
KEY_RIGHT_SHIFT = "rightshift"
KEY_RIGHT_ALT = "rightalt"
KEY_RIGHT_CTRL = "rightctrl"
KEY_RIGHT_SUPER = "rightsuper"
KEY_RIGHT_HYPER = "righthyper"
KEY_RIGHT_META = "rightmeta"
KEY_ISO_LEVEL3_SHIFT = "isolevel3shift"
KEY_ISO_LEVEL5_SHIFT = "isolevel5shift"

# Extended key marker
KEY_EXTENDED = "extended"
