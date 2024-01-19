n = int(input())
commands = input().split()

matrix = []
miner_pos = []  # [miner_row, miner_col]
collected_coal, total_coal = 0, 0

directions = {  # 5 3 -> 5 + (-1), 3 + 0 => 4, 3
    "up": [-1, 0],
    "down": [1, 0],  # [row, col]
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:  # command => down
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
