# Exercise-3:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(nums, target):

    i = 0
    j = 0

    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)):
            if ((nums[i]+nums[j]) == target and (i != j)):
                return (i, j)

numbers = [2, 7, 11, 15]
target_number = 9
print(twoSum(numbers, target_number))

nums = [2,3,4]
target = 6
print(twoSum(nums, target))

nums_1 = [1, 3, 2] 
target_1 = 6
print(twoSum(nums_1, target_1))