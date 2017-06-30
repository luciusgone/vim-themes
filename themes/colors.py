"""Color utils
"""

# keywords of rules
# color set
foreground = "foreground"
background = "background"
selection  = "selection"
line       = "line"
comment    = "comment"
red        = "red"
orange     = "orange"
yellow     = "yellow"
green      = "green"
aqua       = "aqua"
blue       = "blue"
purple     = "purple"
window     = "window"

colorset  = (foreground, background,selection, line, comment, red,
        orange, yellow, green, aqua, blue, purple, window)

class HexColorConv(object):
    """Hex color conversion class
    Borrowed by Tomorrow theme from the theme "Desert256
    Ported to python by Lucius Gone
    """
    def __init__(self, terminal_colors):
        self.terminal_colors = terminal_colors
    def grey_number(self, x):
        """Returns an approximate grey index for the given grey level.
        """
        if self.terminal_colors == 88:
            if   x < 23:  return 0
            elif x < 69:  return 1
            elif x < 103: return 2
            elif x < 127: return 3
            elif x < 150: return 4
            elif x < 173: return 5
            elif x < 196: return 6
            elif x < 219: return 7
            elif x < 243: return 8
            else:         return 9
        else:
            if x < 14:    return 0
            else:
                n = (x - 8) // 10
                m = (x - 8) % 10
                if m < 5: return n
                else:     return n + 1
    def grey_level(self, l):
        """Returns the actual grey level represented by the grey index.
        """
        if self.terminal_colors == 88:
            if   l == 0: return 0
            elif l == 1: return 46
            elif l == 2: return 92
            elif l == 3: return 115
            elif l == 4: return 139
            elif l == 5: return 162
            elif l == 6: return 185
            elif l == 7: return 208
            elif l == 8: return 231
            else:      return 255
        else:
            if l == 0: return 0
            else:      return 8 + l * 10
    def grey_color(self, c):
        """Returns the palette index for the given grey index
        """
        if self.terminal_colors == 88:
            if   c == 0: return 16
            elif c == 9: return 79
            else:        return 79 + c
        else:
            if   c == 0:  return 16
            elif c == 25: return 231
            else:         return 231 + c
    def rgb_number(self, x):
        """Returns an approximate color index for the given color level
        """
        if self.terminal_colors == 88:
            if    x < 69: return 0
            elif x < 172: return 1
            elif x < 230: return 2
            else:         return 3
        else:
            if x < 75: return 0
            else:
                n = (x - 55) // 40
                m = (x - 55) % 40
                if m < 20: return n
                else:      return n + 1
    def rgb_level(self, l):
        """Returns the actual color level for the given color index
        """
        if self.terminal_colors == 88:
            if   l == 0: return 0
            elif l == 1: return 139
            elif l == 2: return 205
            else:      return 255
        else:
            if l == 0: return 0
            else:      return 55 + l * 40
    def rgb_color(self, x, y, z):
        """Returns the palette index for the given R/G/B color indices
        """
        if self.terminal_colors == 88:
            return 16 + (x * 16) + (y * 4) + z
        else:
            return 16 + (x * 36) + (y * 6) + z
    def color(self, r, g, b):
        """Returns the palette index to approximate the given R/G/B color levels
        """
        gx = self.grey_number(r)
        gy = self.grey_number(g)
        gz = self.grey_number(b)

        rx = self.rgb_number(r)
        ry = self.rgb_number(g)
        rz = self.rgb_number(b)

        if gx == gy and gy == gz:
            dgr = self.grey_level(gx) - r
            dgg = self.grey_level(gy) - g
            dgb = self.grey_level(gz) - b
            dgrey = dgr ** 2 + dgg ** 2 + dgb ** 2
            dr = self.rgb_level(gx) - r
            dg = self.rgb_level(gy) - g
            db = self.rgb_level(gz) - b
            drgb = dr ** 2 + dg ** 2 + db ** 2
            if dgrey < drgb:
                return self.grey_color(gx)
            else:
                return self.rgb_color(rx, ry, rz)
        else:
            return self.rgb_color(rx, ry, rz)
    def rgb(self, rgb):
        """Returns the palette index to approximate the 'rrggbb' hex string
        """
        r = int(rgb[0:2], base=16)
        g = int(rgb[2:4], base=16)
        b = int(rgb[4:6], base=16)
        return self.color(r, g, b)

class ColorSet(object):
    """ColorSet for theme.

    Usage:
        cs = ColorSet({'foreground': ['ffffff', '000000']}, 256)
        # gui color
        cs['foreground']
        cs['foreground', True]
        # tui color
        cs['foreground', False]
    """
    def __init__(self, cs, terminal_colors):
        self._cs  = cs
        self._tcs = terminal_colors
        self._conv = HexColorConv(terminal_colors)
    def __getitem__(self, k):
        if isinstance(k, str):
            return self._cs[k][0]
        elif k[1]:
            return self._cs[k[0]][0]
        else:
            return self._conv.rgb(self._cs[k[0]][1])
    def __getattr__(self, name):
        try:
            return self._ansi_esc_str(name)
        except KeyError as e:
            raise AttributeError(e)
    @property
    def palette_board(self):
        global colorset
        bg_str = self._ansi_esc_str("background")
        bg = bg_str * (12 * 6 + 2) + "\n"
        fg = ""
        for color in colorset:
            if color != "background":
                s = self._ansi_esc_str(color)
                fg += bg_str * 2 + s * 4
        fg += bg_str * 2 + "\n"
        pb_str = bg + fg * 2 + bg
        return pb_str
    def _ansi_esc_str(self, name):
        c = self[name, False]
        return f"\033[48;5;{c}m \033[m"

