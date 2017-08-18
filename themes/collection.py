"""Theme Collections
"""

from .scheme import Scheme

tomorrow = Scheme(
    scheme_name = "tomorrow",
    theme_background = "light",
    foreground = ["238", "4d4d4c"],
    background = ["231", "ffffff"],
    selection = ["252", "d6d6d6"],
    line = ["254", "efefef"],
    comment = ["102", "8e908c"],
    red = ["160", "c82829"],
    orange = ["208", "f5871f"],
    yellow = ["178", "eab700"],
    green = ["64", "718c00"],
    aqua = ["31", "3e999f"],
    blue = ["25", "4271ae"],
    purple = ["97", "8959a8"],
    window = ["254", "efefef"]
)

tomorrow_night = Scheme(
    scheme_name = "tomorrow-night",
    theme_background = "dark",
    foreground = ["250", "c5c8c6"],
    background = ["235", "1d1f21"],
    selection = ["239", "373b41"],
    line = ["236", "282a2e"],
    comment = ["245", "969896"],
    red = ["167", "cc6666"],
    orange = ["173", "de935f"],
    yellow = ["222", "f0c674"],
    green = ["143", "b5bd68"],
    aqua = ["109", "8abeb7"],
    blue = ["109", "81a2be"],
    purple = ["139", "b294bb"],
    window = ["240", "4d5057"]
)

tomorrow_night_blue = Scheme(
    scheme_name = "tomorrow-night-blue",
    theme_background = "dark",
    foreground = ["231", "ffffff"],
    background = ["17", "002451"],
    selection = ["18", "003f8e"],
    line = ["17", "00346e"],
    comment = ["67", "7285b7"],
    red = ["217", "ff9da4"],
    orange = ["222", "ffc58f"],
    yellow = ["229", "ffeead"],
    green = ["193", "d1f1a9"],
    aqua = ["123", "99ffff"],
    blue = ["153", "bbdaff"],
    purple = ["219", "ebbbff"],
    window = ["59", "4d5057"]
)

tomorrow_night_bright = Scheme(
    scheme_name = "tomorrow-night-bright",
    theme_background = "dark",
    foreground = ["254", "eaeaea"],
    background = ["16", "000000"],
    selection = ["237", "424242"],
    line = ["234", "2a2a2a"],
    comment = ["245", "969896"],
    red = ["167", "d54e53"],
    orange = ["172", "e78c45"],
    yellow = ["184", "e7c547"],
    green = ["148", "b9ca4a"],
    aqua = ["73", "70c0b1"],
    blue = ["110", "7aa6da"],
    purple = ["176", "c397d8"],
    window = ["59", "4d5057"]
)

tomorrow_night_eighties = Scheme(
    scheme_name = "tomorrow-night-eighties",
    theme_background = "dark",
    foreground = ["251", "cccccc"],
    background = ["235", "2d2d2d"],
    selection = ["238", "515151"],
    line = ["236", "393939"],
    comment = ["246", "999999"],
    red = ["210", "f2777a"],
    orange = ["209", "f99157"],
    yellow = ["221", "ffcc66"],
    green = ["114", "99cc99"],
    aqua = ["80", "66cccc"],
    blue = ["68", "6699cc"],
    purple = ["176", "cc99cc"],
    window = ["59", "4d5057"]
)

all_collection = [
    tomorrow,
    tomorrow_night,
    tomorrow_night_blue,
    tomorrow_night_bright,
    tomorrow_night_eighties,
]
