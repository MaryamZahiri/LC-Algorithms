"""
Pick a random pivot (like in QuickSort).
Partition the array so that:
All elements “larger than” (or “smaller than,” depending on the goal) are on one side.
The pivot ends in its correct final position if the array was fully sorted.
After partitioning, if the pivot position is exactly k–1, you’ve found the k-th largest (or smallest). Otherwise, you recurse only into the half that might still contain the k-th element.
"""
import random

def quickselect(nums, k, largest=True):
    """
    Returns the k-th element (1-based) from nums.
    If largest=True -> k-th largest
    If largest=False -> k-th smallest
    """
    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        
        # Depending on largest or smallest, choose comparison
        for i in range(left, right):
            if (largest and nums[i] > pivot_value) or (not largest and nums[i] < pivot_value):
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot into its final place
        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index
    
    # 1-based k means pivot_index should match k-1 in 0-based
    target_index = k - 1
    left, right = 0, len(nums) - 1
    
    while True:
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
"""
Time:
average O(n)
worst case O(n^2)
- each partition step only removes one element
- n+(n−1)+⋯+1=O(n ^ 2) 
"""