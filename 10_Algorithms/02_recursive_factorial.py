def get_factorial(n: int):
    if n == 0:
        return 1

    return n * get_factorial(n - 1)


n = int(input())
print(get_factorial(n))
