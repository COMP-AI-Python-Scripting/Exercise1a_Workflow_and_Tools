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

friends_shopping_list = shopping_list.copy()

my_new_item = "meatballs"
friends_new_item = "mushrooms"

print(f"Adding {my_new_item} to my shopping list")
shopping_list.append(my_new_item.title())

print(f"Adding {friends_new_item} to my friend's shopping list")
friends_shopping_list.append(friends_new_item.title())

print("My shopping list:")
print(*shopping_list, sep=", ", end="!")

print()

print("My friend's shopping list:")
print(*friends_shopping_list, sep=", ", end="!")
