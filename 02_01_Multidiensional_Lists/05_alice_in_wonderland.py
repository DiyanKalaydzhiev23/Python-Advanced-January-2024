size = int(input())

matrix = []
alice_pos = []

tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "*"

    if element == "R":
        break

    if element.isdigit():
        tea_bags += int(element)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]
