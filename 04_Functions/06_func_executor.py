def func_executor(*funcs_data):
    return "\n".join(f"{func.__name__} - {func(*args)}" for func, args in funcs_data)

# def func_executor(*funcs_data):
#     result = []
#
#     for func, args in funcs_data:
#         result.append(f"{func.__name__} - {func(*args)}")
#
#     return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
