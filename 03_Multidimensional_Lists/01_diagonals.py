n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
second = [matrix[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")
