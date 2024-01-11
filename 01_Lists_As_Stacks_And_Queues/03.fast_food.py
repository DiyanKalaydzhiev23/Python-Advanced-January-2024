from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():  # O(n)
    if food >= order:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left:", *orders)  # " ".join([str(x) for x in orders])
        break
else:
    print("Orders complete")


# solution 2
#
# while orders:
#     order = orders.popleft()
#
#     if food >= order:
#         food -= order
#     else:
#         print(f"Orders left:", order, *orders)  # " ".join([str(x) for x in orders])
#         break
# else:
#     print("Orders complete")