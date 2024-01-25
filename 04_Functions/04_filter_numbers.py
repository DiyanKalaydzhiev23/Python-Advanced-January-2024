def even_odd_filter(**numbers_sets):  # {odd: [1, 2, 3, 4, 10, 5], even: [3, 4, 5, 7, 10, 2, 5, 5, 2]}
    if "odd" in numbers_sets:
        numbers_sets["odd"] = [n for n in numbers_sets["odd"] if n % 2 != 0]

    if "even" in numbers_sets:
        numbers_sets["even"] = [n for n in numbers_sets["even"] if n % 2 == 0]

    return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))
    # numbers_sets.items() => [(odd, [1, 3]), (even, [2, 4])]


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
