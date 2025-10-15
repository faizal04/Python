class Solution:
    nums = [2, 7, 11, 15]
    target = 26
    def twoSums(nums, target):
        hash_map = {2:0, 7:1, 11:2, 15:3}
        for i , num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
        return []
    print(twoSums(nums, target)) 
