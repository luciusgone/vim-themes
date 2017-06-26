"""Tomorrow Night Theme Generator

Original theme from Chris Kempson
Ported to python by Lucius Gone
"""

# theme related variables
scheme_name = "tomorrow-night"
terminal_colors = 256
hi_rules = []

# predefined color set
# default foreground color
foreground = ["c5c8c6", "c5c8c6"]
# default background color
background = ["1d1f21", "303030"]
# default selection color
selection = ["373b41", "585858"]
# default line color
line = ["282a2e", "3a3a3a"]
# default comment color
comment = ["969896", "969896"]
# variables, xml tags, markup link text, markup lists, diff deleted
red = ["cc6666", "cc6666"]
# integers boolean constants, xml attributes, markup lik url
orange = ["de935f", "de935f"]
# classes markup bold search text background
yellow = ["f0c674", "f0c674"]
# strings, inherited class markup code, diff inserted
green = ["b5bd68", "b5bd68"]
# support, regular expressions, escape characters, markup quotes
aqua = ["8abeb7", "8abeb7"]
# functions, methods, attribute ids, headings
blue = ["81a2be", "81a2be"]
# key words, storage, selector, markup italic, diff changed
purple = ["b294bb", "b294bb"]
# invisible
window = ["4d5057", "5e5e5e"]

# attr key words
none = "none"
bold = "bold"
reverse = "reverse"

def grey_number(x):
    """Returns an approximate grey index for the given grey level.
    """
    if terminal_colors == 88:
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

def grey_level(l):
    """Returns the actual grey level represented by the grey index.
    """
    if terminal_colors == 88:
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

def grey_color(c):
    """Returns the palette index for the given grey index
    """
    if terminal_colors == 88:
        if   c == 0: return 16
        elif c == 9: return 79
        else:        return 79 + c
    else:
        if   c == 0:  return 16
        elif c == 25: return 231
        else:         return 231 + c

def rgb_number(x):
    """Returns an approximate color index for the given color level
    """
    if terminal_colors == 88:
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

def rgb_level(l):
    """Returns the actual color level for the given color index
    """
    if terminal_colors == 88:
        if   l == 0: return 0
        elif l == 1: return 139
        elif l == 2: return 205
        else:      return 255
    else:
        if l == 0: return 0
        else:      return 55 + l * 40

def rgb_color(x, y, z):
    """Returns the palette index for the given R/G/B color indices
    """
    if terminal_colors == 88:
        return 16 + (x * 16) + (y * 4) + z
    else:
        return 16 + (x * 36) + (y * 6) + z

def color(r, g, b):
    """Returns the palette index to approximate the given R/G/B color levels
    """
    gx = grey_number(r)
    gy = grey_number(g)
    gz = grey_number(b)

    rx = rgb_number(r)
    ry = rgb_number(g)
    rz = rgb_number(b)

    if gx == gy and gy == gz:
        dgr = grey_level(gx) - r
        dgg = grey_level(gy) - g
        dgb = grey_level(gz) - b
        dgrey = dgr ** 2 + dgg ** 2 + dgb ** 2
        dr = rgb_level(gx) - r
        dg = rgb_level(gy) - g
        db = rgb_level(gz) - b
        drgb = dr ** 2 + dg ** 2 + db ** 2
        if dgrey < drgb:
            return grey_color(gx)
        else:
            return rgb_color(rx, ry, rz)
    else:
        return rgb_color(rx, ry, rz)

def rgb(rgb):
    """Returns the palette index to approximate the 'rrggbb' hex string
    """
    r = int(rgb[0:2], base=16)
    g = int(rgb[2:4], base=16)
    b = int(rgb[4:6], base=16)
    return color(r, g, b)

def hi(group, fg, bg, attr):
    """Returns the highlight command string.
    """
    if fg != None:
        hi_rules.append(f"hi {group} guifg=#{fg[0]} ctermfg={rgb(fg[1])}\n")
    if bg != None:
        hi_rules.append(f"hi {group} guibg=#{bg[0]} ctermbg={rgb(bg[1])}\n")
    if attr != None:
        hi_rules.append(f"hi {group} gui={attr} cterm={attr}\n")

def prelude():
    hi_rules.append("set background=dark\n")
    hi_rules.append("hi clear\n")
    hi_rules.append("syntax reset\n")
    hi_rules.append(f'let g:colors_name="{scheme_name}"\n')
    hi_rules.append("\n")

def generate_hi_rules():
    """Generate the theme rules
    """
    # Vim Highlighting
    hi("Normal", foreground, background, None)
    hi("LineNr", selection, None, None)
    hi("NonText", selection, None, None)
    hi("SpecialKey", selection, None, None)
    hi("Search", background, yellow, None)
    hi("TabLine", window, foreground, reverse)
    hi("TabLineFill", window, foreground, reverse)
    hi("StatusLine", window, yellow, reverse)
    hi("StatusLineNC", window, foreground, reverse)
    hi("VertSplit", window, window, none)
    hi("Visual", None, selection, None)
    hi("Directory", blue, None, None)
    hi("ModeMsg", green, None, None)
    hi("MoreMsg", green, None, None)
    hi("Question", green, None, None)
    hi("WarningMsg", red, None, None)
    hi("MatchParen", None, selection, None)
    hi("Folded", comment, background, None)
    hi("FoldColumn", None, background, None)
    hi("CursorLine", None, line, none)
    hi("CursorColumn", None, line, none)
    hi("PMenu", foreground, selection, none)
    hi("PMenuSel", foreground, selection, reverse)
    hi("SignColumn", None, background, none)
    hi("ColorColumn", None, line, none)

    # Standard Highlighting
    hi("Comment", comment, None, None)
    hi("Todo", comment, background, None)
    hi("Title", comment, None, None)
    hi("Identifier", red, None, none)
    hi("Statement", foreground, None, None)
    hi("Conditional", foreground, None, None)
    hi("Repeat", foreground, None, None)
    hi("Structure", purple, None, None)
    hi("Function", blue, None, None)
    hi("Constant", orange, None, None)
    hi("Keyword", orange, None, None)
    hi("String", green, None, None)
    hi("Special", foreground, None, None)
    hi("PreProc", purple, None, None)
    hi("Operator", aqua, None, none)
    hi("Type", blue, None, none)
    hi("Define", purple, None, none)
    hi("Include", blue, None, None)
    # TODO: find out what this is doing
    # hi("Ignore", "666666", None, None)

    # Vim Highlighting
    hi("vimCommand", red, None, none)

    # C Highlighting
    hi("cType", yellow, None, None)
    hi("cStorageClass", purple, None, None)
    hi("cConditional", purple, None, None)
    hi("cRepeat", purple, None, None)

    # PHP Highlighting
    hi("phpVarSelector", red, None, None)
    hi("phpKeyword", purple, None, None)
    hi("phpRepeat", purple, None, None)
    hi("phpConditional", purple, None, None)
    hi("phpStatement", purple, None, None)
    hi("phpMemberSelector", foreground, None, None)

    # Ruby Highlighting
    hi("rubySymbol", green, None, None)
    hi("rubyConstant", yellow, None, None)
    hi("rubyAccess", yellow, None, None)
    hi("rubyAttribute", blue, None, None)
    hi("rubyInclude", blue, None, None)
    hi("rubyLocalVariableOrMethod", orange, None, None)
    hi("rubyCurlyBlock", orange, None, None)
    hi("rubyStringDelimiter", green, None, None)
    hi("rubyInterpolationDelimiter", orange, None, None)
    hi("rubyConditional", purple, None, None)
    hi("rubyRepeat", purple, None, None)
    hi("rubyControl", purple, None, None)
    hi("rubyException", purple, None, None)

    # Crystal Highlighting
    hi("crystalSymbol", green, None, None)
    hi("crystalConstant", yellow, None, None)
    hi("crystalAccess", yellow, None, None)
    hi("crystalAttribute", blue, None, None)
    hi("crystalInclude", blue, None, None)
    hi("crystalLocalVariableOrMethod", orange, None, None)
    hi("crystalCurlyBlock", orange, None, None)
    hi("crystalStringDelimiter", green, None, None)
    hi("crystalInterpolationDelimiter", orange, None, None)
    hi("crystalConditional", purple, None, None)
    hi("crystalRepeat", purple, None, None)
    hi("crystalControl", purple, None, None)
    hi("crystalException", purple, None, None)

    # Python Highlighting
    hi("pythonInclude", purple, None, None)
    hi("pythonStatement", purple, None, None)
    hi("pythonConditional", purple, None, None)
    hi("pythonRepeat", purple, None, None)
    hi("pythonException", purple, None, None)
    hi("pythonFunction", blue, None, None)
    hi("pythonPreCondit", purple, None, None)
    hi("pythonRepeat", aqua, None, None)
    hi("pythonExClass", orange, None, None)

    # JavaScript Highlighting
    hi("javaScriptBraces", foreground, None, None)
    hi("javaScriptFunction", purple, None, None)
    hi("javaScriptConditional", purple, None, None)
    hi("javaScriptRepeat", purple, None, None)
    hi("javaScriptNumber", orange, None, None)
    hi("javaScriptMember", orange, None, None)
    hi("javascriptNull", orange, None, None)
    hi("javascriptGlobal", blue, None, None)
    hi("javascriptStatement", red, None, None)

    # CoffeeScript Highlighting
    hi("coffeeRepeat", purple, None, None)
    hi("coffeeConditional", purple, None, None)
    hi("coffeeKeyword", purple, None, None)
    hi("coffeeObject", yellow, None, None)

    # HTML Highlighting
    hi("htmlTag", red, None, None)
    hi("htmlTagName", red, None, None)
    hi("htmlArg", red, None, None)
    hi("htmlScriptTag", red, None, None)

    # Diff Highlighting
    # hi("diffAdd", None, "4c4e39", None)
    hi("diffDelete", background, red, None)
    # hi("diffChange", None, "2B5B77", None)
    hi("diffText", line, blue, None)

    # ShowMarks Highlighting
    hi("ShowMarksHLl", orange, background, none)
    hi("ShowMarksHLo", purple, background, none)
    hi("ShowMarksHLu", yellow, background, none)
    hi("ShowMarksHLm", aqua, background, none)

    # Lua Highlighting
    hi("luaStatement", purple, None, None)
    hi("luaRepeat", purple, None, None)
    hi("luaCondStart", purple, None, None)
    hi("luaCondElseif", purple, None, None)
    hi("luaCond", purple, None, None)
    hi("luaCondEnd", purple, None, None)

    # Cucumber Highlighting
    hi("cucumberGiven", blue, None, None)
    hi("cucumberGivenAnd", blue, None, None)

    # Go Highlighting
    hi("goDirective", purple, None, None)
    hi("goDeclaration", purple, None, None)
    hi("goStatement", purple, None, None)
    hi("goConditional", purple, None, None)
    hi("goConstants", orange, None, None)
    hi("goTodo", yellow, None, None)
    hi("goDeclType", blue, None, None)
    hi("goBuiltins", purple, None, None)
    hi("goRepeat", purple, None, None)
    hi("goLabel", purple, None, None)

    # Clojure Highlighting
    hi("clojureConstant", orange, None, None)
    hi("clojureBoolean", orange, None, None)
    hi("clojureCharacter", orange, None, None)
    hi("clojureKeyword", green, None, None)
    hi("clojureNumber", orange, None, None)
    hi("clojureString", green, None, None)
    hi("clojureRegexp", green, None, None)
    hi("clojureParen", aqua, None, None)
    hi("clojureVariable", yellow, None, None)
    hi("clojureCond", blue, None, None)
    hi("clojureDefine", purple, None, None)
    hi("clojureException", red, None, None)
    hi("clojureFunc", blue, None, None)
    hi("clojureMacro", blue, None, None)
    hi("clojureRepeat", blue, None, None)
    hi("clojureSpecial", purple, None, None)
    hi("clojureQuote", blue, None, None)
    hi("clojureUnquote", blue, None, None)
    hi("clojureMeta", blue, None, None)
    hi("clojureDeref", blue, None, None)
    hi("clojureAnonArg", blue, None, None)
    hi("clojureRepeat", blue, None, None)
    hi("clojureDispatch", blue, None, None)

    # Scala Highlighting
    hi("scalaKeyword", purple, None, None)
    hi("scalaKeywordModifier", purple, None, None)
    hi("scalaOperator", blue, None, None)
    hi("scalaPackage", red, None, None)
    hi("scalaFqn", foreground, None, None)
    hi("scalaFqnSet", foreground, None, None)
    hi("scalaImport", purple, None, None)
    hi("scalaBoolean", orange, None, None)
    hi("scalaDef", purple, None, None)
    hi("scalaVal", purple, None, None)
    hi("scalaVar", aqua, None, None)
    hi("scalaClass", purple, None, None)
    hi("scalaObject", purple, None, None)
    hi("scalaTrait", purple, None, None)
    hi("scalaDefName", blue, None, None)
    hi("scalaValName", foreground, None, None)
    hi("scalaVarName", foreground, None, None)
    hi("scalaClassName", foreground, None, None)
    hi("scalaType", yellow, None, None)
    hi("scalaTypeSpecializer", yellow, None, None)
    hi("scalaAnnotation", orange, None, None)
    hi("scalaNumber", orange, None, None)
    hi("scalaDefSpecializer", yellow, None, None)
    hi("scalaClassSpecializer", yellow, None, None)
    hi("scalaBackTick", green, None, None)
    hi("scalaRoot", foreground, None, None)
    hi("scalaMethodCall", blue, None, None)
    hi("scalaCaseType", yellow, None, None)
    hi("scalaLineComment", comment, None, None)
    hi("scalaComment", comment, None, None)
    hi("scalaDocComment", comment, None, None)
    hi("scalaDocTags", comment, None, None)
    hi("scalaEmptyString", green, None, None)
    hi("scalaMultiLineString", green, None, None)
    hi("scalaUnicode", orange, None, None)
    hi("scalaString", green, None, None)
    hi("scalaStringEscape", green, None, None)
    hi("scalaSymbol", orange, None, None)
    hi("scalaChar", orange, None, None)
    hi("scalaXml", green, None, None)
    hi("scalaConstructorSpecializer", yellow, None, None)
    hi("scalaBackTick", blue, None, None)

    # Git
    hi("diffAdded", green, None, None)
    hi("diffRemoved", red, None, None)
    hi("gitcommitSummary", None, None, bold)

def generate():
    """Generate all rules
    """
    prelude()
    generate_hi_rules()

def clear_hi_rules():
    """Clear the theme rules
    """
    hi_rules.clear()

def write_rules_to_file():
    """Write theme rules to file
    """
    with open(f"./colors/{scheme_name}.vim", "w+") as f:
        for rule in hi_rules:
            f.write(rule)

def main():
    """Main entry
    """
    clear_hi_rules()
    generate()
    write_rules_to_file()

# generate the rules immediately
generate()

if __name__ == '__main__':
    main()
