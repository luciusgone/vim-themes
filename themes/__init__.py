from themes.collection import all_collection
from themes.rules import all_rules

for t in all_collection:
    t.add_rules(all_rules)

def generate():
    for t in all_collection:
        print(f"generating theme {t.scheme_name}")
        with open(f"./colors/{t.scheme_name}.vim", "w+") as f:
            f.write(t.common_rules())
            f.write(t.rules())
