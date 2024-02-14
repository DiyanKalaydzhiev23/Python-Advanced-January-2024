def recursive_drawing(n):
    if n == 0:
        return

    print('*' * n)

    recursive_drawing(n - 1)

    print('#' * n)


n = int(input())  # 2
recursive_drawing(n)
