def find_median_sorted(nums):
    n = len(nums)
    mid = n // 2
    
    # If length is even
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    # If length is odd
    else:
        return nums[mid]

# Test
sorted_arr = [1, 3, 3, 6, 7, 8, 9]
print(f"Median: {find_median_sorted(sorted_arr)}") 
# Output: 6