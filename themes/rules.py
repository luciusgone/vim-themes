from themes.colors import (foreground, background,selection, line, comment,
        red, orange, yellow, green, aqua, blue, purple, window)
from themes.keywords import none, bold, reverse

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

all_rules = [
        Rule("Normal", foreground, background, None),
        Rule("LineNr", selection, None, None),
        Rule("NonText", selection, None, None),
        Rule("SpecialKey", selection, None, None),
        Rule("Search", background, yellow, None),
        Rule("TabLine", window, foreground, reverse),
        Rule("TabLineFill", window, foreground, reverse),
        Rule("StatusLine", window, yellow, reverse),
        Rule("StatusLineNC", window, foreground, reverse),
        Rule("VertSplit", window, window, none),
        Rule("Visual", None, selection, None),
        Rule("Directory", blue, None, None),
        Rule("ModeMsg", green, None, None),
        Rule("MoreMsg", green, None, None),
        Rule("Question", green, None, None),
        Rule("WarningMsg", red, None, None),
        Rule("MatchParen", None, selection, None),
        Rule("Folded", comment, background, None),
        Rule("FoldColumn", None, background, None),
        Rule("CursorLine", None, line, none),
        Rule("CursorColumn", None, line, none),
        Rule("PMenu", foreground, selection, none),
        Rule("PMenuSel", foreground, selection, reverse),
        Rule("SignColumn", None, background, none),
        Rule("ColorColumn", None, line, none),

        # Standard Highlighting
        Rule("Comment", comment, None, None),
        Rule("Todo", comment, background, None),
        Rule("Title", comment, None, None),
        Rule("Identifier", red, None, none),
        Rule("Statement", foreground, None, None),
        Rule("Conditional", foreground, None, None),
        Rule("Repeat", foreground, None, None),
        Rule("Structure", purple, None, None),
        Rule("Function", blue, None, None),
        Rule("Constant", orange, None, None),
        Rule("Keyword", orange, None, None),
        Rule("String", green, None, None),
        Rule("Special", foreground, None, None),
        Rule("PreProc", purple, None, None),
        Rule("Operator", aqua, None, none),
        Rule("Type", blue, None, none),
        Rule("Define", purple, None, none),
        Rule("Include", blue, None, None),
        # TODO: find out what this is doing
        # Rule("Ignore", "666666", None, None),

        # Vim Highlighting
        Rule("vimCommand", red, None, none),

        # C Highlighting
        Rule("cType", yellow, None, None),
        Rule("cStorageClass", purple, None, None),
        Rule("cConditional", purple, None, None),
        Rule("cRepeat", purple, None, None),

        # PHP Highlighting
        Rule("phpVarSelector", red, None, None),
        Rule("phpKeyword", purple, None, None),
        Rule("phpRepeat", purple, None, None),
        Rule("phpConditional", purple, None, None),
        Rule("phpStatement", purple, None, None),
        Rule("phpMemberSelector", foreground, None, None),

        # Ruby Highlighting
        Rule("rubySymbol", green, None, None),
        Rule("rubyConstant", yellow, None, None),
        Rule("rubyAccess", yellow, None, None),
        Rule("rubyAttribute", blue, None, None),
        Rule("rubyInclude", blue, None, None),
        Rule("rubyLocalVariableOrMethod", orange, None, None),
        Rule("rubyCurlyBlock", orange, None, None),
        Rule("rubyStringDelimiter", green, None, None),
        Rule("rubyInterpolationDelimiter", orange, None, None),
        Rule("rubyConditional", purple, None, None),
        Rule("rubyRepeat", purple, None, None),
        Rule("rubyControl", purple, None, None),
        Rule("rubyException", purple, None, None),

        # Crystal Highlighting
        Rule("crystalSymbol", green, None, None),
        Rule("crystalConstant", yellow, None, None),
        Rule("crystalAccess", yellow, None, None),
        Rule("crystalAttribute", blue, None, None),
        Rule("crystalInclude", blue, None, None),
        Rule("crystalLocalVariableOrMethod", orange, None, None),
        Rule("crystalCurlyBlock", orange, None, None),
        Rule("crystalStringDelimiter", green, None, None),
        Rule("crystalInterpolationDelimiter", orange, None, None),
        Rule("crystalConditional", purple, None, None),
        Rule("crystalRepeat", purple, None, None),
        Rule("crystalControl", purple, None, None),
        Rule("crystalException", purple, None, None),

        # Python Highlighting
        Rule("pythonInclude", purple, None, None),
        Rule("pythonStatement", purple, None, None),
        Rule("pythonConditional", purple, None, None),
        Rule("pythonRepeat", purple, None, None),
        Rule("pythonException", purple, None, None),
        Rule("pythonFunction", blue, None, None),
        Rule("pythonPreCondit", purple, None, None),
        Rule("pythonRepeat", aqua, None, None),
        Rule("pythonExClass", orange, None, None),

        # JavaScript Highlighting
        Rule("javaScriptBraces", foreground, None, None),
        Rule("javaScriptFunction", purple, None, None),
        Rule("javaScriptConditional", purple, None, None),
        Rule("javaScriptRepeat", purple, None, None),
        Rule("javaScriptNumber", orange, None, None),
        Rule("javaScriptMember", orange, None, None),
        Rule("javascriptNull", orange, None, None),
        Rule("javascriptGlobal", blue, None, None),
        Rule("javascriptStatement", red, None, None),

        # CoffeeScript Highlighting
        Rule("coffeeRepeat", purple, None, None),
        Rule("coffeeConditional", purple, None, None),
        Rule("coffeeKeyword", purple, None, None),
        Rule("coffeeObject", yellow, None, None),

        # HTML Highlighting
        Rule("htmlTag", red, None, None),
        Rule("htmlTagName", red, None, None),
        Rule("htmlArg", red, None, None),
        Rule("htmlScriptTag", red, None, None),

        # Diff Highlighting
        # Rule("diffAdd", None, "4c4e39", None),
        Rule("diffDelete", background, red, None),
        # Rule("diffChange", None, "2B5B77", None),
        Rule("diffText", line, blue, None),

        # ShowMarks Highlighting
        Rule("ShowMarksHLl", orange, background, none),
        Rule("ShowMarksHLo", purple, background, none),
        Rule("ShowMarksHLu", yellow, background, none),
        Rule("ShowMarksHLm", aqua, background, none),

        # Lua Highlighting
        Rule("luaStatement", purple, None, None),
        Rule("luaRepeat", purple, None, None),
        Rule("luaCondStart", purple, None, None),
        Rule("luaCondElseif", purple, None, None),
        Rule("luaCond", purple, None, None),
        Rule("luaCondEnd", purple, None, None),

        # Cucumber Highlighting
        Rule("cucumberGiven", blue, None, None),
        Rule("cucumberGivenAnd", blue, None, None),

        # Go Highlighting
        Rule("goDirective", purple, None, None),
        Rule("goDeclaration", purple, None, None),
        Rule("goStatement", purple, None, None),
        Rule("goConditional", purple, None, None),
        Rule("goConstants", orange, None, None),
        Rule("goTodo", yellow, None, None),
        Rule("goDeclType", blue, None, None),
        Rule("goBuiltins", purple, None, None),
        Rule("goRepeat", purple, None, None),
        Rule("goLabel", purple, None, None),

        # Clojure Highlighting
        Rule("clojureConstant", orange, None, None),
        Rule("clojureBoolean", orange, None, None),
        Rule("clojureCharacter", orange, None, None),
        Rule("clojureKeyword", green, None, None),
        Rule("clojureNumber", orange, None, None),
        Rule("clojureString", green, None, None),
        Rule("clojureRegexp", green, None, None),
        Rule("clojureParen", aqua, None, None),
        Rule("clojureVariable", yellow, None, None),
        Rule("clojureCond", blue, None, None),
        Rule("clojureDefine", purple, None, None),
        Rule("clojureException", red, None, None),
        Rule("clojureFunc", blue, None, None),
        Rule("clojureMacro", blue, None, None),
        Rule("clojureRepeat", blue, None, None),
        Rule("clojureSpecial", purple, None, None),
        Rule("clojureQuote", blue, None, None),
        Rule("clojureUnquote", blue, None, None),
        Rule("clojureMeta", blue, None, None),
        Rule("clojureDeref", blue, None, None),
        Rule("clojureAnonArg", blue, None, None),
        Rule("clojureRepeat", blue, None, None),
        Rule("clojureDispatch", blue, None, None),

        # Scala Highlighting
        Rule("scalaKeyword", purple, None, None),
        Rule("scalaKeywordModifier", purple, None, None),
        Rule("scalaOperator", blue, None, None),
        Rule("scalaPackage", red, None, None),
        Rule("scalaFqn", foreground, None, None),
        Rule("scalaFqnSet", foreground, None, None),
        Rule("scalaImport", purple, None, None),
        Rule("scalaBoolean", orange, None, None),
        Rule("scalaDef", purple, None, None),
        Rule("scalaVal", purple, None, None),
        Rule("scalaVar", aqua, None, None),
        Rule("scalaClass", purple, None, None),
        Rule("scalaObject", purple, None, None),
        Rule("scalaTrait", purple, None, None),
        Rule("scalaDefName", blue, None, None),
        Rule("scalaValName", foreground, None, None),
        Rule("scalaVarName", foreground, None, None),
        Rule("scalaClassName", foreground, None, None),
        Rule("scalaType", yellow, None, None),
        Rule("scalaTypeSpecializer", yellow, None, None),
        Rule("scalaAnnotation", orange, None, None),
        Rule("scalaNumber", orange, None, None),
        Rule("scalaDefSpecializer", yellow, None, None),
        Rule("scalaClassSpecializer", yellow, None, None),
        Rule("scalaBackTick", green, None, None),
        Rule("scalaRoot", foreground, None, None),
        Rule("scalaMethodCall", blue, None, None),
        Rule("scalaCaseType", yellow, None, None),
        Rule("scalaLineComment", comment, None, None),
        Rule("scalaComment", comment, None, None),
        Rule("scalaDocComment", comment, None, None),
        Rule("scalaDocTags", comment, None, None),
        Rule("scalaEmptyString", green, None, None),
        Rule("scalaMultiLineString", green, None, None),
        Rule("scalaUnicode", orange, None, None),
        Rule("scalaString", green, None, None),
        Rule("scalaStringEscape", green, None, None),
        Rule("scalaSymbol", orange, None, None),
        Rule("scalaChar", orange, None, None),
        Rule("scalaXml", green, None, None),
        Rule("scalaConstructorSpecializer", yellow, None, None),
        Rule("scalaBackTick", blue, None, None),

        # Git
        Rule("diffAdded", green, None, None),
        Rule("diffRemoved", red, None, None),
        Rule("gitcommitSummary", None, None, bold),
        ]
