from typing import List


def print_numbers(nums: List[int]) -> None:
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)

    print(negative_sum)
    print(positive_sum)

    if positive_sum > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
print_numbers(numbers)
