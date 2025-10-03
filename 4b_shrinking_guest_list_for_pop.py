guests = ['albert einstein', 'rosalind franklin', 'linus pauling']

for name in guests:
    print(f"{name.title()}, please come to dinner.")


print(f"\nSorry, {guests[1].title()} can't make it to dinner.\n")

del guests[1]

guests.insert(1, 'kurt godel')

for name in guests:
    print(f"{name.title()}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'elda emma anderson')
guests.insert(2, 'stephen hawking')
guests.append('roger penrose')

for name in guests:
    print(f"{name.title()}, please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

length = len(guests)
for _ in range(2, length):
    uninvited = guests.pop()
    print(f"Sorry, {uninvited.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
for name in guests:
    print(f"{name.title()}, please come to dinner.")

# Empty out the list.
del (guests[0])
del (guests[0])

# Prove the list is empty.
print(f'The guest list for the dinner party is empty {guests}')
