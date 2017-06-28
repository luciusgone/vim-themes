from themes.utils import Theme

tomorrow = Theme(
        scheme_name = "tomorrow",
        theme_background = "light",
        terminal_colors = 256,
        # color set
        foreground = ["4d4d4c", "4d4d4c"],
        background = ["ffffff", "ffffff"],
        selection = ["d6d6d6", "d6d6d6"],
        line = ["efefef", "efefef"],
        comment = ["8e908c", "8e908c"],
        red = ["c82829", "c82829"],
        orange = ["f5871f", "f5871f"],
        yellow = ["eab700", "eab700"],
        green = ["718c00", "718c00"],
        aqua = ["3e999f", "3e999f"],
        blue = ["4271ae", "4271ae"],
        purple = ["8959a8", "8959a8"],
        window = ["efefef", "efefef"]
)

tomorrow_night = Theme(
        scheme_name = "tomorrow-night",
        theme_background = "dark",
        terminal_colors = 256,
        # color set
        foreground = ["c5c8c6", "c5c8c6"],
        background = ["1d1f21", "303030"],
        selection = ["373b41", "585858"],
        line = ["282a2e", "3a3a3a"],
        comment = ["969896", "969896"],
        red = ["cc6666", "cc6666"],
        orange = ["de935f", "de935f"],
        yellow = ["f0c674", "f0c674"],
        green = ["b5bd68", "b5bd68"],
        aqua = ["8abeb7", "8abeb7"],
        blue = ["81a2be", "81a2be"],
        purple = ["b294bb", "b294bb"],
        window = ["4d5057", "5e5e5e"]
)

tomorrow_night_blue = Theme(
        scheme_name = "tomorrow-night-blue",
        theme_background = "dark",
        terminal_colors = 256,
        # color set
        foreground = ["ffffff", "ffffff"],
        background = ["002451", "002451"],
        selection = ["003f8e", "003f8e"],
        line = ["00346e", "00346e"],
        comment = ["7285b7", "7285b7"],
        red = ["ff9da4", "ff9da4"],
        orange = ["ffc58f", "ffc58f"],
        yellow = ["ffeead", "ffeead"],
        green = ["d1f1a9", "d1f1a9"],
        aqua = ["99ffff", "99ffff"],
        blue = ["bbdaff", "bbdaff"],
        purple = ["ebbbff", "ebbbff"],
        window = ["4d5057", "4d5057"]
)

tomorrow_night_bright = Theme(
        scheme_name = "tomorrow-night-bright",
        theme_background = "dark",
        terminal_colors = 256,
        # color set
        foreground = ["eaeaea", "eaeaea"],
        background = ["000000", "000000"],
        selection = ["424242", "424242"],
        line = ["2a2a2a", "2a2a2a"],
        comment = ["969896", "969896"],
        red = ["d54e53", "d54e53"],
        orange = ["e78c45", "e78c45"],
        yellow = ["e7c547", "e7c547"],
        green = ["b9ca4a", "b9ca4a"],
        aqua = ["70c0b1", "70c0b1"],
        blue = ["7aa6da", "7aa6da"],
        purple = ["c397d8", "c397d8"],
        window = ["4d5057", "4d5057"]
)

tomorrow_night_eighties = Theme(
        scheme_name = "tomorrow-night-eighties",
        theme_background = "dark",
        terminal_colors = 256,
        # color set
        foreground = ["cccccc", "cccccc"],
        background = ["2d2d2d", "2d2d2d"],
        selection = ["515151", "515151"],
        line = ["393939", "393939"],
        comment = ["999999", "999999"],
        red = ["f2777a", "f2777a"],
        orange = ["f99157", "f99157"],
        yellow = ["ffcc66", "ffcc66"],
        green = ["99cc99", "99cc99"],
        aqua = ["66cccc", "66cccc"],
        blue = ["6699cc", "6699cc"],
        purple = ["cc99cc", "cc99cc"],
        window = ["4d5057", "4d5057"]
)

all_collection = (tomorrow, tomorrow_night, tomorrow_night_blue,
        tomorrow_night_bright, tomorrow_night_eighties)
