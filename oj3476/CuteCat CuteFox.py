"""3476"""
import ast
n = int(input())
cat = {}
fox = {}

for _ in range(n):
    data = ast.literal_eval(input())
    for name, code in data.items():
        if code.startswith("Cat"):
            cat[code] = name
        elif code.startswith("Fox"):
            fox[code] = name

all_names = set(cat.values()) | set(fox.values())

if "Cat01" not in cat and "Garfield" not in all_names:
    cat["Cat01"] = "Garfield"
if "Fox01" not in fox and "Fubuki" not in all_names:
    fox["Fox01"] = "Fubuki"

print(f"Cat : {len(cat)}")
print(f"Fox : {len(fox)}")

for code in sorted(cat, key=lambda x: int(x[3:])):
    print(f"{cat[code]} : {code}")
for code in sorted(fox, key=lambda x: int(x[3:])):
    print(f"{fox[code]} : {code}")
