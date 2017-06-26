#!/usr/bin/env python3

import themes
import themes.generator as generator

def write_theme_file(theme):
    """Write theme rules to file.
    """
    with open(f"./colors/{theme.scheme_name}.vim", "w+") as f:
        for rule in theme.hi_rules:
            f.write(rule)

def main():
    for theme in themes.all_themes:
        g = generator.generate_hi_rules(theme)
        write_theme_file(g)

if __name__ == "__main__":
    main()

