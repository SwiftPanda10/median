# Author: Samuel Bennett
# Date: 4/28/2021
# Description: Function named find_median takes a list of numbers and returns the statistical median of those numbers

some_nums = [13, 7, -3, 82, 4]


def find_median(some_nums):
    some_nums.sort()
    if len(some_nums) % 2 != 0:
        median = some_nums[int(len(some_nums)/2)]
    else:
        median = some_nums[int(len(some_nums)/2) - 1] + some_nums[int(len(some_nums)/2)]
        median = median/2
    return median


result = find_median(some_nums)

print(result)
