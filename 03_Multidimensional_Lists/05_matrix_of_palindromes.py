rows, cols = [int(x) for x in input().split()]

start = ord('a')

for row in range(start, start + rows):
    for col in range(row, row + cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()
