from .collection import all_collection
from .rules import all_rules


for t in all_collection:
    t.add_rules(all_rules)


def generate(theme):
    if theme == 'all':
        for t in all_collection:
            write_theme_to_file(t)
    else:
        for t in all_collection:
            if theme == t.scheme_name:
                write_theme_to_file(t)


def write_theme_to_file(t):
    print(f"generating theme {t.scheme_name}")
    with open(f"./colors/{t.scheme_name}.vim", "w+") as f:
        f.write(str(t))


def print_color_palette(theme):
    if theme == 'all':
        for t in all_collection:
            print_palette_board(t)
    else:
        for t in all_collection:
            if theme == t.scheme_name:
                print_palette_board(t)


def print_palette_board(t):
    print(f"{t.scheme_name}:\n")
    print(t.palette_board)
