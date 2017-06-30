from themes.colors import HexColorConv, ColorSet

class HiRule(object):
    def __init__(self, rule, color_set):
        self.group = rule.group
        self.guifg = color_set[rule.fg] if rule.fg else None
        self.ctermfg = color_set[rule.fg, False] if rule.fg else None
        self.guibg = color_set[rule.bg] if rule.bg else None
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
    def __init__(self, scheme_name, theme_background, terminal_colors, **cs):
        self.scheme_name      = scheme_name
        self.theme_background = theme_background
        self.terminal_colors  = terminal_colors
        self.hi_rules         = {}
        self.color_set        = ColorSet(cs, terminal_colors)
    def add_rules(self, rules):
        for rule in rules:
            hi = HiRule(rule, self.color_set)
            self.hi_rules[rule.group] = hi
    def rule(self, name):
        return self.hi_rules[name]
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
