def spy(nums):
    for index, num in enumerate(nums):
        if num == 0 and nums[index+1] == 0 and nums[index+2] == 7:
            return True

    return False

print(spy([2, 3, 4, 0, 0, 7, 5, 6, 3, 4, 5, 6]))

