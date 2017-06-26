"""Theme Generator
"""

class HexColorConverter(object):
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

class Generator(object):
    def __init__(self, theme):
        self.theme = theme
        self.scheme_name = theme.scheme_name
        self.hi_rules = []
        self.terminal_colors = theme.terminal_colors
        self.converter = HexColorConverter(theme.terminal_colors)
        self.append_common_rules()
    def append_common_rules(self):
        t = self.theme
        self.hi_rules.append("hi clear\n")
        self.hi_rules.append("syntax reset\n")
        self.hi_rules.append(f"set background={t.theme_background}\n")
        self.hi_rules.append(f'let g:colors_name="{t.scheme_name}"\n')
        self.hi_rules.append("\n")
    def rgb(self, c):
        return self.converter.rgb(c)
    def hi(self, group, fg , bg, attr):
        """Returns the highlight command string.
        """
        t = self.terminal_colors
        if fg != None:
            guifg = fg[0]
            ctermfg = self.rgb(fg[1])
            r = f"hi {group} guifg=#{guifg} ctermfg={ctermfg}\n"
            self.hi_rules.append(r)
        if bg != None:
            guibg = bg[0]
            ctermbg = self.rgb(bg[1])
            r = f"hi {group} guibg=#{guibg} ctermbg={ctermbg}\n"
            self.hi_rules.append(r)
        if attr != None:
            self.hi_rules.append(f"hi {group} gui={attr} cterm={attr}\n")
    def clear_hi_rules(self):
        self.hi_rules.clear()

def generate_hi_rules(theme):
    """Generate the theme rules
    """
    foreground = theme.foreground
    background = theme.background
    selection = theme.selection
    line = theme.line
    comment = theme.comment
    red = theme.red
    orange = theme.orange
    yellow = theme.yellow
    green = theme.green
    aqua = theme.aqua
    blue = theme.blue
    purple = theme.purple
    window = theme.window
    # attr key words
    none = "none"
    bold = "bold"
    reverse = "reverse"

    g = Generator(theme)

    # Vim Highlighting
    g.hi("Normal", foreground, background, None)
    g.hi("LineNr", selection, None, None)
    g.hi("NonText", selection, None, None)
    g.hi("SpecialKey", selection, None, None)
    g.hi("Search", background, yellow, None)
    g.hi("TabLine", window, foreground, reverse)
    g.hi("TabLineFill", window, foreground, reverse)
    g.hi("StatusLine", window, yellow, reverse)
    g.hi("StatusLineNC", window, foreground, reverse)
    g.hi("VertSplit", window, window, none)
    g.hi("Visual", None, selection, None)
    g.hi("Directory", blue, None, None)
    g.hi("ModeMsg", green, None, None)
    g.hi("MoreMsg", green, None, None)
    g.hi("Question", green, None, None)
    g.hi("WarningMsg", red, None, None)
    g.hi("MatchParen", None, selection, None)
    g.hi("Folded", comment, background, None)
    g.hi("FoldColumn", None, background, None)
    g.hi("CursorLine", None, line, none)
    g.hi("CursorColumn", None, line, none)
    g.hi("PMenu", foreground, selection, none)
    g.hi("PMenuSel", foreground, selection, reverse)
    g.hi("SignColumn", None, background, none)
    g.hi("ColorColumn", None, line, none)

    # Standard Highlighting
    g.hi("Comment", comment, None, None)
    g.hi("Todo", comment, background, None)
    g.hi("Title", comment, None, None)
    g.hi("Identifier", red, None, none)
    g.hi("Statement", foreground, None, None)
    g.hi("Conditional", foreground, None, None)
    g.hi("Repeat", foreground, None, None)
    g.hi("Structure", purple, None, None)
    g.hi("Function", blue, None, None)
    g.hi("Constant", orange, None, None)
    g.hi("Keyword", orange, None, None)
    g.hi("String", green, None, None)
    g.hi("Special", foreground, None, None)
    g.hi("PreProc", purple, None, None)
    g.hi("Operator", aqua, None, none)
    g.hi("Type", blue, None, none)
    g.hi("Define", purple, None, none)
    g.hi("Include", blue, None, None)
    # TODO: find out what this is doing
    # g.hi("Ignore", "666666", None, None)

    # Vim Highlighting
    g.hi("vimCommand", red, None, none)

    # C Highlighting
    g.hi("cType", yellow, None, None)
    g.hi("cStorageClass", purple, None, None)
    g.hi("cConditional", purple, None, None)
    g.hi("cRepeat", purple, None, None)

    # PHP Highlighting
    g.hi("phpVarSelector", red, None, None)
    g.hi("phpKeyword", purple, None, None)
    g.hi("phpRepeat", purple, None, None)
    g.hi("phpConditional", purple, None, None)
    g.hi("phpStatement", purple, None, None)
    g.hi("phpMemberSelector", foreground, None, None)

    # Ruby Highlighting
    g.hi("rubySymbol", green, None, None)
    g.hi("rubyConstant", yellow, None, None)
    g.hi("rubyAccess", yellow, None, None)
    g.hi("rubyAttribute", blue, None, None)
    g.hi("rubyInclude", blue, None, None)
    g.hi("rubyLocalVariableOrMethod", orange, None, None)
    g.hi("rubyCurlyBlock", orange, None, None)
    g.hi("rubyStringDelimiter", green, None, None)
    g.hi("rubyInterpolationDelimiter", orange, None, None)
    g.hi("rubyConditional", purple, None, None)
    g.hi("rubyRepeat", purple, None, None)
    g.hi("rubyControl", purple, None, None)
    g.hi("rubyException", purple, None, None)

    # Crystal Highlighting
    g.hi("crystalSymbol", green, None, None)
    g.hi("crystalConstant", yellow, None, None)
    g.hi("crystalAccess", yellow, None, None)
    g.hi("crystalAttribute", blue, None, None)
    g.hi("crystalInclude", blue, None, None)
    g.hi("crystalLocalVariableOrMethod", orange, None, None)
    g.hi("crystalCurlyBlock", orange, None, None)
    g.hi("crystalStringDelimiter", green, None, None)
    g.hi("crystalInterpolationDelimiter", orange, None, None)
    g.hi("crystalConditional", purple, None, None)
    g.hi("crystalRepeat", purple, None, None)
    g.hi("crystalControl", purple, None, None)
    g.hi("crystalException", purple, None, None)

    # Python Highlighting
    g.hi("pythonInclude", purple, None, None)
    g.hi("pythonStatement", purple, None, None)
    g.hi("pythonConditional", purple, None, None)
    g.hi("pythonRepeat", purple, None, None)
    g.hi("pythonException", purple, None, None)
    g.hi("pythonFunction", blue, None, None)
    g.hi("pythonPreCondit", purple, None, None)
    g.hi("pythonRepeat", aqua, None, None)
    g.hi("pythonExClass", orange, None, None)

    # JavaScript Highlighting
    g.hi("javaScriptBraces", foreground, None, None)
    g.hi("javaScriptFunction", purple, None, None)
    g.hi("javaScriptConditional", purple, None, None)
    g.hi("javaScriptRepeat", purple, None, None)
    g.hi("javaScriptNumber", orange, None, None)
    g.hi("javaScriptMember", orange, None, None)
    g.hi("javascriptNull", orange, None, None)
    g.hi("javascriptGlobal", blue, None, None)
    g.hi("javascriptStatement", red, None, None)

    # CoffeeScript Highlighting
    g.hi("coffeeRepeat", purple, None, None)
    g.hi("coffeeConditional", purple, None, None)
    g.hi("coffeeKeyword", purple, None, None)
    g.hi("coffeeObject", yellow, None, None)

    # HTML Highlighting
    g.hi("htmlTag", red, None, None)
    g.hi("htmlTagName", red, None, None)
    g.hi("htmlArg", red, None, None)
    g.hi("htmlScriptTag", red, None, None)

    # Diff Highlighting
    # g.hi("diffAdd", None, "4c4e39", None)
    g.hi("diffDelete", background, red, None)
    # g.hi("diffChange", None, "2B5B77", None)
    g.hi("diffText", line, blue, None)

    # ShowMarks Highlighting
    g.hi("ShowMarksHLl", orange, background, none)
    g.hi("ShowMarksHLo", purple, background, none)
    g.hi("ShowMarksHLu", yellow, background, none)
    g.hi("ShowMarksHLm", aqua, background, none)

    # Lua Highlighting
    g.hi("luaStatement", purple, None, None)
    g.hi("luaRepeat", purple, None, None)
    g.hi("luaCondStart", purple, None, None)
    g.hi("luaCondElseif", purple, None, None)
    g.hi("luaCond", purple, None, None)
    g.hi("luaCondEnd", purple, None, None)

    # Cucumber Highlighting
    g.hi("cucumberGiven", blue, None, None)
    g.hi("cucumberGivenAnd", blue, None, None)

    # Go Highlighting
    g.hi("goDirective", purple, None, None)
    g.hi("goDeclaration", purple, None, None)
    g.hi("goStatement", purple, None, None)
    g.hi("goConditional", purple, None, None)
    g.hi("goConstants", orange, None, None)
    g.hi("goTodo", yellow, None, None)
    g.hi("goDeclType", blue, None, None)
    g.hi("goBuiltins", purple, None, None)
    g.hi("goRepeat", purple, None, None)
    g.hi("goLabel", purple, None, None)

    # Clojure Highlighting
    g.hi("clojureConstant", orange, None, None)
    g.hi("clojureBoolean", orange, None, None)
    g.hi("clojureCharacter", orange, None, None)
    g.hi("clojureKeyword", green, None, None)
    g.hi("clojureNumber", orange, None, None)
    g.hi("clojureString", green, None, None)
    g.hi("clojureRegexp", green, None, None)
    g.hi("clojureParen", aqua, None, None)
    g.hi("clojureVariable", yellow, None, None)
    g.hi("clojureCond", blue, None, None)
    g.hi("clojureDefine", purple, None, None)
    g.hi("clojureException", red, None, None)
    g.hi("clojureFunc", blue, None, None)
    g.hi("clojureMacro", blue, None, None)
    g.hi("clojureRepeat", blue, None, None)
    g.hi("clojureSpecial", purple, None, None)
    g.hi("clojureQuote", blue, None, None)
    g.hi("clojureUnquote", blue, None, None)
    g.hi("clojureMeta", blue, None, None)
    g.hi("clojureDeref", blue, None, None)
    g.hi("clojureAnonArg", blue, None, None)
    g.hi("clojureRepeat", blue, None, None)
    g.hi("clojureDispatch", blue, None, None)

    # Scala Highlighting
    g.hi("scalaKeyword", purple, None, None)
    g.hi("scalaKeywordModifier", purple, None, None)
    g.hi("scalaOperator", blue, None, None)
    g.hi("scalaPackage", red, None, None)
    g.hi("scalaFqn", foreground, None, None)
    g.hi("scalaFqnSet", foreground, None, None)
    g.hi("scalaImport", purple, None, None)
    g.hi("scalaBoolean", orange, None, None)
    g.hi("scalaDef", purple, None, None)
    g.hi("scalaVal", purple, None, None)
    g.hi("scalaVar", aqua, None, None)
    g.hi("scalaClass", purple, None, None)
    g.hi("scalaObject", purple, None, None)
    g.hi("scalaTrait", purple, None, None)
    g.hi("scalaDefName", blue, None, None)
    g.hi("scalaValName", foreground, None, None)
    g.hi("scalaVarName", foreground, None, None)
    g.hi("scalaClassName", foreground, None, None)
    g.hi("scalaType", yellow, None, None)
    g.hi("scalaTypeSpecializer", yellow, None, None)
    g.hi("scalaAnnotation", orange, None, None)
    g.hi("scalaNumber", orange, None, None)
    g.hi("scalaDefSpecializer", yellow, None, None)
    g.hi("scalaClassSpecializer", yellow, None, None)
    g.hi("scalaBackTick", green, None, None)
    g.hi("scalaRoot", foreground, None, None)
    g.hi("scalaMethodCall", blue, None, None)
    g.hi("scalaCaseType", yellow, None, None)
    g.hi("scalaLineComment", comment, None, None)
    g.hi("scalaComment", comment, None, None)
    g.hi("scalaDocComment", comment, None, None)
    g.hi("scalaDocTags", comment, None, None)
    g.hi("scalaEmptyString", green, None, None)
    g.hi("scalaMultiLineString", green, None, None)
    g.hi("scalaUnicode", orange, None, None)
    g.hi("scalaString", green, None, None)
    g.hi("scalaStringEscape", green, None, None)
    g.hi("scalaSymbol", orange, None, None)
    g.hi("scalaChar", orange, None, None)
    g.hi("scalaXml", green, None, None)
    g.hi("scalaConstructorSpecializer", yellow, None, None)
    g.hi("scalaBackTick", blue, None, None)

    # Git
    g.hi("diffAdded", green, None, None)
    g.hi("diffRemoved", red, None, None)
    g.hi("gitcommitSummary", None, None, bold)

    return g
