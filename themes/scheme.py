from .keywords import colorset


class ColorSet(object):
    """ColorSet for theme.

    Usage:
        cs = ColorSet({'foreground': ['1', '000000']})
        # gui color
        cs['foreground', True]
        # tui color
        cs['foreground', False]
    """
    def __init__(self, cs):
        self._cs = cs
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
    def __str__(self):
        global colorset
        pb_str = ""
        for color in colorset:
            s = self._ansi_esc_str(color)
            pb_str += s * 4
        pb_str += "\n"
        return pb_str
    def _ansi_esc_str(self, name):
        c = self[name, False]
        return f"\033[48;5;{c}m \033[m"


class Rule(object):
    """Generic rules
    """
    def __init__(self, group, fg, bg, attr, guisp):
        self.group = group
        self.fg    = fg
        self.bg    = bg
        self.attr  = attr
        self.guisp = guisp
    def __repr__(self):
        s = "<Rule group:{} foreground:{}, background:{}, attr:{}, guisp:{}>"
        return s.format(self.group, self.fg, self.bg, self.attr, self.guisp)


class HiRule(object):
    def __init__(self, rule, color_set):
        self.group = rule.group
        self.guifg = color_set[rule.fg, True] if rule.fg else None
        self.ctermfg = color_set[rule.fg, False] if rule.fg else None
        self.guibg = color_set[rule.bg, True] if rule.bg else None
        self.ctermbg = color_set[rule.bg, False] if rule.bg else None
        self.attr = rule.attr if rule.attr else None
        self.guisp = color_set[rule.guisp, True] if rule.guisp else None
    def __str__(self):
        g = f"hi {self.group}"
        gf = f" guifg=#{self.guifg}" if self.guifg else ""
        gb = f" guibg=#{self.guibg}" if self.guibg else ""
        tf = f" ctermfg={self.ctermfg}" if self.ctermfg else ""
        tb = f" ctermbg={self.ctermbg}" if self.ctermbg else ""
        ga = f" gui={self.attr}" if self.attr else ""
        ta = f" cterm={self.attr}" if self.attr else ""
        gsp = f" guisp=#{self.guisp}" if self.guisp else ""
        eol = "\n"
        return g + gf + gb + ga + tf + tb + ta + gsp + eol


class Scheme(object):
    def __init__(self, scheme_name, theme_background, **cs):
        self.scheme_name      = scheme_name
        self.theme_background = theme_background
        self.hi_rules         = {}
        self.color_set        = ColorSet(cs)
        self.palette_board    = str(self.color_set)
    def add_rules(self, rules):
        for rule in rules:
            hi = HiRule(rule, self.color_set)
            self.hi_rules[rule.group.lower()] = hi
    def rule(self, name):
        return self.hi_rules[name]
    def hi_rule(self, name):
        return self.hi_rules[name.lower()]
    def __str__(self):
        rule_str = ""
        rule_str += "hi clear\n"
        rule_str += "syntax reset\n"
        rule_str += f"set background={self.theme_background}\n"
        rule_str += f'let g:colors_name="{self.scheme_name}"\n'
        rule_str += "\n"
        for name in self.hi_rules:
            rule_str += str(self.hi_rules[name])
        return rule_str
    def __repr__(self):
        return "<Scheme scheme_name='{}'>".format(self.scheme_name)
