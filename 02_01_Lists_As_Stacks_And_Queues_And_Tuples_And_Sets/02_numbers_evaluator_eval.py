from collections import deque
from math import floor

expression = deque(input().split())  # [6, 5, -, 4, 5, +]

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        for _ in range(idx - 1):
            expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))

        del expression[1]
        idx = 1

    idx += 1

print(floor(int(expression[0])))
