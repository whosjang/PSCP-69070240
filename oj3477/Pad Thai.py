"""3477"""
ingredient = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

flavor = {"Sweet", "Sour", "Salty"}

used = set()
taste = set()

while True:
    item = input()
    if item == "Cook":
        break
    used.add(item)

while True:
    eat = input()
    if eat == "End":
        break
    taste.add(eat)

if not used.issubset(ingredient):
    print("This is not Pad Thai!!!")
elif used != ingredient:
    print("This is bad!")
elif taste != flavor:
    print("Not Bad...")
else:
    print("Delicious!")
