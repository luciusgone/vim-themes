from .collection import all_collection
from .rules import all_rules

for t in all_collection:
    t.add_rules(all_rules)

def generate():
    # TODO: we can specify a scheme to generate
    for t in all_collection:
        print(f"generating theme {t.scheme_name}")
        with open(f"./colors/{t.scheme_name}.vim", "w+") as f:
            f.write(t.common_rules)
            f.write(t.rules)

def print_color_palette():
    # TODO: we can print a specific palette
    for t in all_collection:
        print(f"{t.scheme_name}:\n")
        print(t.palette_board)

def get_hi_rule(theme, rule):
    # TODO: implement this
    pass
