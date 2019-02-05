from .keywords import *
from .scheme import Rule


all_rules = [
# Vim editor colors
    Rule("Normal",        base05, base00, None, None),
    Rule("Bold",          None,   None,   bold, None),
    Rule("Debug",         base08, None,   None, None),
    Rule("Directory",     base0D, None,   None, None),
    Rule("Error",         base00, base08, None, None),
    Rule("ErrorMsg",      base08, base00, None, None),
    Rule("Exception",     base08, None,   None, None),
    Rule("FoldColumn",    base0C, base01, None, None),
    Rule("Folded",        base03, base01, None, None),
    Rule("IncSearch",     base01, base09, none, None),
    Rule("Italic",        None,   None,   none, None),
    Rule("Macro",         base08, None,   None, None),
    Rule("MatchParen",    None,   base03, None, None),
    Rule("ModeMsg",       base0B, None,   None, None),
    Rule("MoreMsg",       base0B, None,   None, None),
    Rule("Question",      base0D, None,   None, None),
    Rule("Search",        base01, base0A, None, None),
    Rule("Substitute",    base01, base0A, none, None),
    Rule("SpecialKey",    base03, None,   None, None),
    Rule("TooLong",       base08, None,   None, None),
    Rule("Underlined",    base08, None,   None, None),
    Rule("Visual",        None,   base02, None, None),
    Rule("VisualNOS",     base08, None,   None, None),
    Rule("WarningMsg",    base08, None,   None, None),
    Rule("WildMenu",      base08, base0A, None, None),
    Rule("Title",         base0D, None,   none, None),
    Rule("Conceal",       base0D, base00, None, None),
    Rule("Cursor",        base00, base05, None, None),
    Rule("NonText",       base03, None,   None, None),
    Rule("LineNr",        base03, base01, None, None),
    Rule("SignColumn",    base03, base01, None, None),
    Rule("StatusLine",    base04, base02, none, None),
    Rule("StatusLineNC",  base03, base01, none, None),
    Rule("VertSplit",     base02, base02, none, None),
    Rule("ColorColumn",   None,   base01, none, None),
    Rule("CursorColumn",  None,   base01, none, None),
    Rule("CursorLine",    None,   base01, none, None),
    Rule("CursorLineNr",  base04, base01, None, None),
    Rule("QuickFixLine",  None,   base01, none, None),
    Rule("PMenu",         base05, base01, none, None),
    Rule("PMenuSel",      base01, base05, None, None),
    Rule("TabLine",       base03, base01, none, None),
    Rule("TabLineFill",   base03, base01, none, None),
    Rule("TabLineSel",    base0B, base01, none, None),

# Standard syntax highlighting
    Rule("Boolean",      base09, None,   None, None),
    Rule("Character",    base08, None,   None, None),
    Rule("Comment",      base03, None,   None, None),
    Rule("Conditional",  base0E, None,   None, None),
    Rule("Constant",     base09, None,   None, None),
    Rule("Define",       base0E, None,   none, None),
    Rule("Delimiter",    base0F, None,   None, None),
    Rule("Float",        base09, None,   None, None),
    Rule("Function",     base0D, None,   None, None),
    Rule("Identifier",   base08, None,   none, None),
    Rule("Include",      base0D, None,   None, None),
    Rule("Keyword",      base0E, None,   None, None),
    Rule("Label",        base0A, None,   None, None),
    Rule("Number",       base09, None,   None, None),
    Rule("Operator",     base05, None,   none, None),
    Rule("PreProc",      base0A, None,   None, None),
    Rule("Repeat",       base0A, None,   None, None),
    Rule("Special",      base0C, None,   None, None),
    Rule("SpecialChar",  base0F, None,   None, None),
    Rule("Statement",    base08, None,   None, None),
    Rule("StorageClass", base0A, None,   None, None),
    Rule("String",       base0B, None,   None, None),
    Rule("Structure",    base0E, None,   None, None),
    Rule("Tag",          base0A, None,   None, None),
    Rule("Todo",         base0A, base01, None, None),
    Rule("Type",         base0A, None,   none, None),
    Rule("Typedef",      base0A, None,   None, None),

# C highlighting
    Rule("cOperator",   base0C, None, None, None),
    Rule("cPreCondit",  base0E, None, None, None),

# C# highlighting
    Rule("csClass",                 base0A, None, None, None),
    Rule("csAttribute",             base0A, None, None, None),
    Rule("csModifier",              base0E, None, None, None),
    Rule("csType",                  base08, None, None, None),
    Rule("csUnspecifiedStatement",  base0D, None, None, None),
    Rule("csContextualStatement",   base0E, None, None, None),
    Rule("csNewDecleration",        base08, None, None, None),

# CSS highlighting
    Rule("cssBraces",      base05, None, None, None),
    Rule("cssClassName",   base0E, None, None, None),
    Rule("cssColor",       base0C, None, None, None),

# Diff highlighting
    Rule("DiffAdd",      base0B, base01, None, None),
    Rule("DiffChange",   base03, base01, None, None),
    Rule("DiffDelete",   base08, base01, None, None),
    Rule("DiffText",     base0D, base01, None, None),
    Rule("DiffAdded",    base0B, base00, None, None),
    Rule("DiffFile",     base08, base00, None, None),
    Rule("DiffNewFile",  base0B, base00, None, None),
    Rule("DiffLine",     base0D, base00, None, None),
    Rule("DiffRemoved",  base08, base00, None, None),

# Git highlighting
    Rule("gitcommitOverflow",       base08, None, None, None),
    Rule("gitcommitSummary",        base0B, None, None, None),
    Rule("gitcommitComment",        base03, None, None, None),
    Rule("gitcommitUntracked",      base03, None, None, None),
    Rule("gitcommitDiscarded",      base03, None, None, None),
    Rule("gitcommitSelected",       base03, None, None, None),
    Rule("gitcommitHeader",         base0E, None, None, None),
    Rule("gitcommitSelectedType",   base0D, None, None, None),
    Rule("gitcommitUnmergedType",   base0D, None, None, None),
    Rule("gitcommitDiscardedType",  base0D, None, None, None),
    Rule("gitcommitBranch",         base09, None, bold, None),
    Rule("gitcommitUntrackedFile",  base0A, None, None, None),
    Rule("gitcommitUnmergedFile",   base08, None, bold, None),
    Rule("gitcommitDiscardedFile",  base08, None, bold, None),
    Rule("gitcommitSelectedFile",   base0B, None, bold, None),

# GitGutter highlighting
    Rule("GitGutterAdd",            base0B, base01, None, None),
    Rule("GitGutterChange",         base0D, base01, None, None),
    Rule("GitGutterDelete",         base08, base01, None, None),
    Rule("GitGutterChangeDelete",   base0E, base01, None, None),

# HTML highlighting
    Rule("htmlBold",    base0A, None, None, None),
    Rule("htmlItalic",  base0E, None, None, None),
    Rule("htmlEndTag",  base05, None, None, None),
    Rule("htmlTag",     base05, None, None, None),

# JavaScript highlighting
    Rule("javaScript",        base05, None, None, None),
    Rule("javaScriptBraces",  base05, None, None, None),
    Rule("javaScriptNumber",  base09, None, None, None),
# pangloss/vim-javascript highlighting
    Rule("jsOperator",          base0D, None, None, None),
    Rule("jsStatement",         base0E, None, None, None),
    Rule("jsReturn",            base0E, None, None, None),
    Rule("jsThis",              base08, None, None, None),
    Rule("jsClassDefinition",   base0A, None, None, None),
    Rule("jsFunction",          base0E, None, None, None),
    Rule("jsFuncName",          base0D, None, None, None),
    Rule("jsFuncCall",          base0D, None, None, None),
    Rule("jsClassFuncName",     base0D, None, None, None),
    Rule("jsClassMethodType",   base0E, None, None, None),
    Rule("jsRegexpString",      base0C, None, None, None),
    Rule("jsGlobalObjects",     base0A, None, None, None),
    Rule("jsGlobalNodeObjects", base0A, None, None, None),
    Rule("jsExceptions",        base0A, None, None, None),
    Rule("jsBuiltins",          base0A, None, None, None),

# Mail highlighting
    Rule("mailQuoted1",  base0A, None, None, None),
    Rule("mailQuoted2",  base0B, None, None, None),
    Rule("mailQuoted3",  base0E, None, None, None),
    Rule("mailQuoted4",  base0C, None, None, None),
    Rule("mailQuoted5",  base0D, None, None, None),
    Rule("mailQuoted6",  base0A, None, None, None),
    Rule("mailURL",      base0D, None, None, None),
    Rule("mailEmail",    base0D, None, None, None),

# Markdown highlighting
    Rule("markdownCode",              base0B, None,   None, None),
    Rule("markdownError",             base05, base00, None, None),
    Rule("markdownCodeBlock",         base0B, None,   None, None),
    Rule("markdownHeadingDelimiter",  base0D, None,   None, None),

# NERDTree highlighting
    Rule("NERDTreeDirSlash",  base0D, None, None, None),
    Rule("NERDTreeExecFile",  base05, None, None, None),

# PHP highlighting
    Rule("phpMemberSelector",  base05, None, None, None),
    Rule("phpComparison",      base05, None, None, None),
    Rule("phpParent",          base05, None, None, None),
    Rule("phpMethodsVar",      base0C, None, None, None),

# Python highlighting
    Rule("pythonOperator",  base0E, None, None, None),
    Rule("pythonRepeat",    base0E, None, None, None),
    Rule("pythonInclude",   base0E, None, None, None),
    Rule("pythonStatement", base0E, None, None, None),

# Ruby highlighting
    Rule("rubyAttribute",               base0D, None, None, None),
    Rule("rubyConstant",                base0A, None, None, None),
    Rule("rubyInterpolationDelimiter",  base0F, None, None, None),
    Rule("rubyRegexp",                  base0C, None, None, None),
    Rule("rubySymbol",                  base0B, None, None, None),
    Rule("rubyStringDelimiter",         base0B, None, None, None),

# SASS highlighting
    Rule("sassidChar",     base08, None, None, None),
    Rule("sassClassChar",  base09, None, None, None),
    Rule("sassInclude",    base0E, None, None, None),
    Rule("sassMixing",     base0E, None, None, None),
    Rule("sassMixinName",  base0D, None, None, None),

# Signify highlighting
    Rule("SignifySignAdd",     base0B, base01, None, None),
    Rule("SignifySignChange",  base0D, base01, None, None),
    Rule("SignifySignDelete",  base08, base01, None, None),

# Spelling highlighting
    Rule("SpellBad",     None, None, undercurl, base08),
    Rule("SpellLocal",   None, None, undercurl, base0C),
    Rule("SpellCap",     None, None, undercurl, base0D),
    Rule("SpellRare",    None, None, undercurl, base0E),

# Startify highlighting
    Rule("StartifyBracket",  base03, None, None, None),
    Rule("StartifyFile",     base07, None, None, None),
    Rule("StartifyFooter",   base03, None, None, None),
    Rule("StartifyHeader",   base0B, None, None, None),
    Rule("StartifyNumber",   base09, None, None, None),
    Rule("StartifyPath",     base03, None, None, None),
    Rule("StartifySection",  base0E, None, None, None),
    Rule("StartifySelect",   base0C, None, None, None),
    Rule("StartifySlash",    base03, None, None, None),
    Rule("StartifySpecial",  base03, None, None, None),

# Java highlighting
    Rule("javaOperator",     base0D, None, None, None),

]
