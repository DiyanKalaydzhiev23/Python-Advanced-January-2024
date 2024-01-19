def check_indices_valid(indices):  # row1=1 col1=2 row2=0 col2=2
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)

def swap_elements(command, indices):
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices  # [2, 5, 3, 4]
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]  # row => [1, 2, 3, 4] =>
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]  # row = 3, col = 4
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)  # [0, 1, 2]
valid_cols = range(cols)  # [0, 1, 2, 3]

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]  # ["swap", 2, 3, 5, 4]

    if command_type == "END":
        break

    swap_elements(command_type, coordinates)