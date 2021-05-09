nums = [2,2]
target = 4

# Double for loop. Brute force. O(n^2)
def twoSum_brute_force(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
            
            
# Double for loop, .index(). Brute force. O(n^2)
# This doesn't work because .index() does not account for duplicates!
def twoSum_brute_force_index(nums, target):
    for i in nums[:-1]:
        for j in nums[1:]:
            if i + j == target:
                return nums.index(i), nums.index(j)
            
# Double for loop, .enumerate(). Brute force. O(n^2)
def two_sum_brute_force_enumerate(nums, target):
    seen = set()
    for i in enumerate(nums):
        seen.add(i)
        for j in enumerate(nums):
            if i[1] + j[1] == target and j not in seen :
                return (i[0],j[0])

# Dictionary O(n)
# Higher memory usage as you would need to store things
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return (seen[target-num], i)
        elif num not in seen:
            seen[num] = i

# print(twoSum_brute_force(nums, target))
# print(twoSum_brute_force_index(nums, target))
# print(two_sum_brute_force_enumerate(nums, target))
print(twoSum(nums, target))