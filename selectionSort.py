import random

def selectSort(nums):
    amount = len(nums)

    for i in range(amount):
        smallest = nums[i]
        toSwap = i

        for j in range(amount):
            if nums[j] < smallest and j > i:
                smallest = nums[j]
                toSwap = j

        temp = nums[i]
        nums[i] = smallest
        nums[toSwap] = temp 

    return nums

nums = []

for i in range(10):
    nums.append(random.randint(0,20))

print(nums, "\n\n\n\n")
print(selectSort(nums))
