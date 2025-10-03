guests = ['albert einstein', 'rosalind franklin', 'linus pauling']

for name in guests:
    print(f"{name.title()}, please come to dinner.")


print(f"\nSorry, {guests[1].title()} can't make it to dinner.\n")
guests[1] = 'kurt godel'


for name in guests:
    print(f"{name.title()}, please come to dinner.")
