# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# word = list(input())
#
# word_copy = deque(word)
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#
#     if row % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")
#

# solution 2

from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)
multiplier = 1

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    print(*[word_copy.popleft() for _ in range(cols)][::multiplier], sep="")
    multiplier *= -1
