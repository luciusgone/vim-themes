hi clear
syntax reset
set background=dark
let g:colors_name="tomorrow-night-eighties"

hi Normal guifg=#cccccc guibg=#2d2d2d ctermfg=251 ctermbg=235
hi LineNr guifg=#515151 ctermfg=238
hi NonText guifg=#515151 ctermfg=238
hi SpecialKey guifg=#515151 ctermfg=238
hi Search guifg=#2d2d2d guibg=#ffcc66 ctermfg=235 ctermbg=221
hi TabLine guifg=#4d5057 guibg=#cccccc gui=reverse ctermfg=59 ctermbg=251 cterm=reverse
hi TabLineFill guifg=#4d5057 guibg=#cccccc gui=reverse ctermfg=59 ctermbg=251 cterm=reverse
hi StatusLine guifg=#4d5057 guibg=#ffcc66 gui=reverse ctermfg=59 ctermbg=221 cterm=reverse
hi StatusLineNC guifg=#4d5057 guibg=#cccccc gui=reverse ctermfg=59 ctermbg=251 cterm=reverse
hi VertSplit guifg=#4d5057 guibg=#4d5057 gui=none ctermfg=59 ctermbg=59 cterm=none
hi Visual guibg=#515151 ctermbg=238
hi Directory guifg=#6699cc ctermfg=68
hi ModeMsg guifg=#99cc99 ctermfg=114
hi MoreMsg guifg=#99cc99 ctermfg=114
hi Question guifg=#99cc99 ctermfg=114
hi WarningMsg guifg=#f2777a ctermfg=210
hi MatchParen guibg=#515151 ctermbg=238
hi Folded guifg=#999999 guibg=#2d2d2d ctermfg=246 ctermbg=235
hi FoldColumn guibg=#2d2d2d ctermbg=235
hi CursorLine guibg=#393939 gui=none ctermbg=236 cterm=none
hi CursorColumn guibg=#393939 gui=none ctermbg=236 cterm=none
hi PMenu guifg=#cccccc guibg=#515151 gui=none ctermfg=251 ctermbg=238 cterm=none
hi PMenuSel guifg=#cccccc guibg=#515151 gui=reverse ctermfg=251 ctermbg=238 cterm=reverse
hi SignColumn guibg=#2d2d2d gui=none ctermbg=235 cterm=none
hi ColorColumn guibg=#393939 gui=none ctermbg=236 cterm=none
hi Comment guifg=#999999 ctermfg=246
hi Todo guifg=#999999 guibg=#2d2d2d ctermfg=246 ctermbg=235
hi Title guifg=#999999 ctermfg=246
hi Identifier guifg=#f2777a gui=none ctermfg=210 cterm=none
hi Statement guifg=#cccccc ctermfg=251
hi Conditional guifg=#cccccc ctermfg=251
hi Repeat guifg=#cccccc ctermfg=251
hi Structure guifg=#cc99cc ctermfg=176
hi Function guifg=#6699cc ctermfg=68
hi Constant guifg=#f99157 ctermfg=209
hi Keyword guifg=#f99157 ctermfg=209
hi String guifg=#99cc99 ctermfg=114
hi Special guifg=#cccccc ctermfg=251
hi PreProc guifg=#cc99cc ctermfg=176
hi Operator guifg=#66cccc gui=none ctermfg=80 cterm=none
hi Type guifg=#6699cc gui=none ctermfg=68 cterm=none
hi Define guifg=#cc99cc gui=none ctermfg=176 cterm=none
hi Include guifg=#6699cc ctermfg=68
hi vimCommand guifg=#f2777a gui=none ctermfg=210 cterm=none
hi cType guifg=#ffcc66 ctermfg=221
hi cStorageClass guifg=#cc99cc ctermfg=176
hi cConditional guifg=#cc99cc ctermfg=176
hi cRepeat guifg=#cc99cc ctermfg=176
hi phpVarSelector guifg=#f2777a ctermfg=210
hi phpKeyword guifg=#cc99cc ctermfg=176
hi phpRepeat guifg=#cc99cc ctermfg=176
hi phpConditional guifg=#cc99cc ctermfg=176
hi phpStatement guifg=#cc99cc ctermfg=176
hi phpMemberSelector guifg=#cccccc ctermfg=251
hi rubySymbol guifg=#99cc99 ctermfg=114
hi rubyConstant guifg=#ffcc66 ctermfg=221
hi rubyAccess guifg=#ffcc66 ctermfg=221
hi rubyAttribute guifg=#6699cc ctermfg=68
hi rubyInclude guifg=#6699cc ctermfg=68
hi rubyLocalVariableOrMethod guifg=#f99157 ctermfg=209
hi rubyCurlyBlock guifg=#f99157 ctermfg=209
hi rubyStringDelimiter guifg=#99cc99 ctermfg=114
hi rubyInterpolationDelimiter guifg=#f99157 ctermfg=209
hi rubyConditional guifg=#cc99cc ctermfg=176
hi rubyRepeat guifg=#cc99cc ctermfg=176
hi rubyControl guifg=#cc99cc ctermfg=176
hi rubyException guifg=#cc99cc ctermfg=176
hi crystalSymbol guifg=#99cc99 ctermfg=114
hi crystalConstant guifg=#ffcc66 ctermfg=221
hi crystalAccess guifg=#ffcc66 ctermfg=221
hi crystalAttribute guifg=#6699cc ctermfg=68
hi crystalInclude guifg=#6699cc ctermfg=68
hi crystalLocalVariableOrMethod guifg=#f99157 ctermfg=209
hi crystalCurlyBlock guifg=#f99157 ctermfg=209
hi crystalStringDelimiter guifg=#99cc99 ctermfg=114
hi crystalInterpolationDelimiter guifg=#f99157 ctermfg=209
hi crystalConditional guifg=#cc99cc ctermfg=176
hi crystalRepeat guifg=#cc99cc ctermfg=176
hi crystalControl guifg=#cc99cc ctermfg=176
hi crystalException guifg=#cc99cc ctermfg=176
hi pythonInclude guifg=#cc99cc ctermfg=176
hi pythonStatement guifg=#cc99cc ctermfg=176
hi pythonConditional guifg=#cc99cc ctermfg=176
hi pythonRepeat guifg=#66cccc ctermfg=80
hi pythonException guifg=#cc99cc ctermfg=176
hi pythonFunction guifg=#6699cc ctermfg=68
hi pythonPreCondit guifg=#cc99cc ctermfg=176
hi pythonExClass guifg=#f99157 ctermfg=209
hi javaScriptBraces guifg=#cccccc ctermfg=251
hi javaScriptFunction guifg=#cc99cc ctermfg=176
hi javaScriptConditional guifg=#cc99cc ctermfg=176
hi javaScriptRepeat guifg=#cc99cc ctermfg=176
hi javaScriptNumber guifg=#f99157 ctermfg=209
hi javaScriptMember guifg=#f99157 ctermfg=209
hi javascriptNull guifg=#f99157 ctermfg=209
hi javascriptGlobal guifg=#6699cc ctermfg=68
hi javascriptStatement guifg=#f2777a ctermfg=210
hi coffeeRepeat guifg=#cc99cc ctermfg=176
hi coffeeConditional guifg=#cc99cc ctermfg=176
hi coffeeKeyword guifg=#cc99cc ctermfg=176
hi coffeeObject guifg=#ffcc66 ctermfg=221
hi htmlTag guifg=#f2777a ctermfg=210
hi htmlTagName guifg=#f2777a ctermfg=210
hi htmlArg guifg=#f2777a ctermfg=210
hi htmlScriptTag guifg=#f2777a ctermfg=210
hi diffDelete guifg=#2d2d2d guibg=#f2777a ctermfg=235 ctermbg=210
hi diffText guifg=#393939 guibg=#6699cc ctermfg=236 ctermbg=68
hi ShowMarksHLl guifg=#f99157 guibg=#2d2d2d gui=none ctermfg=209 ctermbg=235 cterm=none
hi ShowMarksHLo guifg=#cc99cc guibg=#2d2d2d gui=none ctermfg=176 ctermbg=235 cterm=none
hi ShowMarksHLu guifg=#ffcc66 guibg=#2d2d2d gui=none ctermfg=221 ctermbg=235 cterm=none
hi ShowMarksHLm guifg=#66cccc guibg=#2d2d2d gui=none ctermfg=80 ctermbg=235 cterm=none
hi luaStatement guifg=#cc99cc ctermfg=176
hi luaRepeat guifg=#cc99cc ctermfg=176
hi luaCondStart guifg=#cc99cc ctermfg=176
hi luaCondElseif guifg=#cc99cc ctermfg=176
hi luaCond guifg=#cc99cc ctermfg=176
hi luaCondEnd guifg=#cc99cc ctermfg=176
hi cucumberGiven guifg=#6699cc ctermfg=68
hi cucumberGivenAnd guifg=#6699cc ctermfg=68
hi goDirective guifg=#cc99cc ctermfg=176
hi goDeclaration guifg=#cc99cc ctermfg=176
hi goStatement guifg=#cc99cc ctermfg=176
hi goConditional guifg=#cc99cc ctermfg=176
hi goConstants guifg=#f99157 ctermfg=209
hi goTodo guifg=#ffcc66 ctermfg=221
hi goDeclType guifg=#6699cc ctermfg=68
hi goBuiltins guifg=#cc99cc ctermfg=176
hi goRepeat guifg=#cc99cc ctermfg=176
hi goLabel guifg=#cc99cc ctermfg=176
hi clojureConstant guifg=#f99157 ctermfg=209
hi clojureBoolean guifg=#f99157 ctermfg=209
hi clojureCharacter guifg=#f99157 ctermfg=209
hi clojureKeyword guifg=#99cc99 ctermfg=114
hi clojureNumber guifg=#f99157 ctermfg=209
hi clojureString guifg=#99cc99 ctermfg=114
hi clojureRegexp guifg=#99cc99 ctermfg=114
hi clojureParen guifg=#66cccc ctermfg=80
hi clojureVariable guifg=#ffcc66 ctermfg=221
hi clojureCond guifg=#6699cc ctermfg=68
hi clojureDefine guifg=#cc99cc ctermfg=176
hi clojureException guifg=#f2777a ctermfg=210
hi clojureFunc guifg=#6699cc ctermfg=68
hi clojureMacro guifg=#6699cc ctermfg=68
hi clojureRepeat guifg=#6699cc ctermfg=68
hi clojureSpecial guifg=#cc99cc ctermfg=176
hi clojureQuote guifg=#6699cc ctermfg=68
hi clojureUnquote guifg=#6699cc ctermfg=68
hi clojureMeta guifg=#6699cc ctermfg=68
hi clojureDeref guifg=#6699cc ctermfg=68
hi clojureAnonArg guifg=#6699cc ctermfg=68
hi clojureDispatch guifg=#6699cc ctermfg=68
hi scalaKeyword guifg=#cc99cc ctermfg=176
hi scalaKeywordModifier guifg=#cc99cc ctermfg=176
hi scalaOperator guifg=#6699cc ctermfg=68
hi scalaPackage guifg=#f2777a ctermfg=210
hi scalaFqn guifg=#cccccc ctermfg=251
hi scalaFqnSet guifg=#cccccc ctermfg=251
hi scalaImport guifg=#cc99cc ctermfg=176
hi scalaBoolean guifg=#f99157 ctermfg=209
hi scalaDef guifg=#cc99cc ctermfg=176
hi scalaVal guifg=#cc99cc ctermfg=176
hi scalaVar guifg=#66cccc ctermfg=80
hi scalaClass guifg=#cc99cc ctermfg=176
hi scalaObject guifg=#cc99cc ctermfg=176
hi scalaTrait guifg=#cc99cc ctermfg=176
hi scalaDefName guifg=#6699cc ctermfg=68
hi scalaValName guifg=#cccccc ctermfg=251
hi scalaVarName guifg=#cccccc ctermfg=251
hi scalaClassName guifg=#cccccc ctermfg=251
hi scalaType guifg=#ffcc66 ctermfg=221
hi scalaTypeSpecializer guifg=#ffcc66 ctermfg=221
hi scalaAnnotation guifg=#f99157 ctermfg=209
hi scalaNumber guifg=#f99157 ctermfg=209
hi scalaDefSpecializer guifg=#ffcc66 ctermfg=221
hi scalaClassSpecializer guifg=#ffcc66 ctermfg=221
hi scalaBackTick guifg=#6699cc ctermfg=68
hi scalaRoot guifg=#cccccc ctermfg=251
hi scalaMethodCall guifg=#6699cc ctermfg=68
hi scalaCaseType guifg=#ffcc66 ctermfg=221
hi scalaLineComment guifg=#999999 ctermfg=246
hi scalaComment guifg=#999999 ctermfg=246
hi scalaDocComment guifg=#999999 ctermfg=246
hi scalaDocTags guifg=#999999 ctermfg=246
hi scalaEmptyString guifg=#99cc99 ctermfg=114
hi scalaMultiLineString guifg=#99cc99 ctermfg=114
hi scalaUnicode guifg=#f99157 ctermfg=209
hi scalaString guifg=#99cc99 ctermfg=114
hi scalaStringEscape guifg=#99cc99 ctermfg=114
hi scalaSymbol guifg=#f99157 ctermfg=209
hi scalaChar guifg=#f99157 ctermfg=209
hi scalaXml guifg=#99cc99 ctermfg=114
hi scalaConstructorSpecializer guifg=#ffcc66 ctermfg=221
hi diffAdded guifg=#99cc99 ctermfg=114
hi diffRemoved guifg=#f2777a ctermfg=210
hi gitcommitSummary gui=bold cterm=bold
