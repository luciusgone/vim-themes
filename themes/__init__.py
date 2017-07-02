from themes.collection import all_collection
from themes.rules import all_rules

for t in all_collection:
    r = all_collection[t]
    r.add_rules(all_rules)

def generate():
    # TODO: we can specify a scheme to generate
    for t in all_collection:
        r = all_collection[t]
        print(f"generating theme {r.scheme_name}")
        with open(f"./colors/{r.scheme_name}.vim", "w+") as f:
            f.write(r.common_rules)
            f.write(r.rules)

def print_color_palette():
    # TODO: we can print a specific palette
    for t in all_collection:
        r = all_collection[t]
        print(f"{r.scheme_name}:\n")
        print(r.palette_board)

def get_hi_rule(theme, rule):
    # TODO: implement this
    pass
