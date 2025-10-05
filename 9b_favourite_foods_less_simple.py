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

shopping_list = [item.title() for item in shopping_list]

print("My shopping list:")
print(*shopping_list, sep=", ", end="!")

print("\nThe first three items in my shopping list:")
print(*shopping_list[0:3], sep=", ", end="!")

print("\nThe next three items in my shopping list:")
print(*shopping_list[3:6], sep=", ", end="!")

print("\nThe last three items in my shopping list:")
print(*shopping_list[6:], sep=", ", end="!")
