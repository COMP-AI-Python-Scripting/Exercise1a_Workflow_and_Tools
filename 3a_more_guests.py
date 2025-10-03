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
