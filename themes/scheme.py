from .keywords import colorset


class ColorSet(object):
    """ColorSet for theme.

    Usage:
        cs = ColorSet({'foreground': ['ffffff', '000000']}, 256)
        # gui color
        cs['foreground', True]
        # tui color
        cs['foreground', False]
    """
    def __init__(self, cs):
        self._cs  = cs
    def __getitem__(self, k):
        if isinstance(k, tuple):
            if k[1]:
                return self._cs[k[0]][1]
            else:
                return self._cs[k[0]][0]
        else:
            raise TypeError("tuple is madontory")
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


class Rule(object):
    """Generic rules
    """
    def __init__(self, group, fg, bg, attr):
        self.group = group
        self.fg    = fg
        self.bg    = bg
        self.attr  = attr
    def __str__(self):
        s = "group {} -> foreground: {}, background: {}, attr: {}"
        return s.format(self.group, self.fg, self.bg, self.attr)


class HiRule(object):
    def __init__(self, rule, color_set):
        self.group = rule.group
        self.guifg = color_set[rule.fg, True] if rule.fg else None
        self.ctermfg = color_set[rule.fg, False] if rule.fg else None
        self.guibg = color_set[rule.bg, True] if rule.bg else None
        self.ctermbg = color_set[rule.bg, False] if rule.bg else None
        self.attr = rule.attr if rule.attr else None
    def __str__(self):
        g = f"hi {self.group}"
        gf = f" guifg=#{self.guifg}" if self.guifg else ""
        gb = f" guibg=#{self.guibg}" if self.guibg else ""
        tf = f" ctermfg={self.ctermfg}" if self.ctermfg else ""
        tb = f" ctermbg={self.ctermbg}" if self.ctermbg else ""
        ga = f" gui={self.attr}" if self.attr else ""
        ta = f" cterm={self.attr}" if self.attr else ""
        eol = "\n"
        return g + gf + gb + ga + tf + tb + ta + eol


class Scheme(object):
    def __init__(self, scheme_name, theme_background, **cs):
        self.scheme_name      = scheme_name
        self.theme_background = theme_background
        self.hi_rules         = {}
        self.color_set        = ColorSet(cs)
    def add_rules(self, rules):
        for rule in rules:
            hi = HiRule(rule, self.color_set)
            self.hi_rules[rule.group.lower()] = hi
    def rule(self, name):
        return self.hi_rules[name]
    def hi_rule(self, name):
        # TODO this returned hi rules should be escaped to the correct color
        return self.hi_rules[name.lower()]
    @property
    def rules(self):
        rule_str = ""
        for name in self.hi_rules:
            rule_str += str(self.hi_rules[name])
        return rule_str
    @property
    def common_rules(self):
        cr_str = ""
        cr_str += "hi clear\n"
        cr_str += "syntax reset\n"
        cr_str += f"set background={self.theme_background}\n"
        cr_str += f'let g:colors_name="{self.scheme_name}"\n'
        cr_str += "\n"
        return cr_str
    @property
    def palette_board(self):
        return self.color_set.palette_board
