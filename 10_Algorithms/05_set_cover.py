def set_cover(universe, sets):
    chosen_sets = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(best_set)
        universe -= best_set

    return chosen_sets


universe = {int(x) for x in input().split(", ")}
num_sets = int(input())
sets = [{int(x) for x in input().split(", ")} for _ in range(num_sets)]

result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print("{ " + f"{', '.join(str(x) for x in s)}" + " }") for s in result]
