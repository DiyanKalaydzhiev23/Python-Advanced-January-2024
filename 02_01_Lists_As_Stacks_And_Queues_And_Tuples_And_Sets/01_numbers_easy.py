first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [first_set.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_set.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_set.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_set.discard(int(el)) for el in data]
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
