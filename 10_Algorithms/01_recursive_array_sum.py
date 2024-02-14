def calc_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calc_sum(nums, idx + 1)


nums = [int(x) for x in input().split()]
print(calc_sum(nums))
