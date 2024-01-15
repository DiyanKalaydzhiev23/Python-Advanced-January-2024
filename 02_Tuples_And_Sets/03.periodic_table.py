table = set()

for _ in range(int(input())):
    for el in input().split():  # input().split() -> ["Ce", "O", "H"]
        table.add(el)

print(*table, sep="\n")


# print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")
# not a good idea
