def insertion_sort(nums):
    for i in range(1, len(nums)):  # започваме от 1, защото на 0 е сортираната част
        key = nums[i]  # взимаме key, защото при разместването, ще се загуби
        j = i - 1  # взимаме последната стойност на сортираната част

        # докато не стигнем началото
        # и докато не стигнем позиция, на която да поставим ключа
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shift-ваме елемента
            j -= 1  # местим се наляво

        nums[j + 1] = key  # слагаме ключа на валидната позиция


nums = [int(x) for x in input().split()]
insertion_sort(nums)
print(*nums)
