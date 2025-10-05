shopping_list = [
    "eggs",
    "milk",
    "pasta",
    "cheese",
    "olives",
    "feta cheese",
    "olive oil",
    "basil",
    "flour",
]

print("My shopping list:")
for food in shopping_list:
    print(f"{food}", end=", ")

print()

print("\nThe first three items in my shopping list:")
for food in shopping_list[0:3]:
    print(f"{food}", end=", ")

print("\nThe next three items in my shopping list:")
for food in shopping_list[3:6]:
    print(f"{food}", end=", ")

print()

print("\nThe last three items in my shopping list:")
for food in shopping_list[6:]:
    print(f"{food}", end=", ")

print()
