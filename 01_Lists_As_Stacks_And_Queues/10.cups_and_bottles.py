from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])

wasted_liters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_liters += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *bottles)

print(f"Wasted litters of water: {wasted_liters}")
