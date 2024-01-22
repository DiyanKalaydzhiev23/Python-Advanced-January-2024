from typing import List


def move(direction: str, steps: int) -> List[int]:
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction: str) -> List[int] or None:
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
field = []

targets = 0
targets_hit = 0

targets_hit_positions = []
my_position = []  # [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]

    targets += field[row].count("x")

for _ in range(int(input())):
    command_info = input().split()  # "move up 4" -> ["move", "up", "4"]

    if command_info[0] == "move":
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])  # [row, col] | None

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep="\n")  # [[1, 2], [3, 4]] ->
