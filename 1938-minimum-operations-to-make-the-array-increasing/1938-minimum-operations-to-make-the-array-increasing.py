

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                operations += increment
                nums[i] = nums[i - 1] + 1  # Update the current element
                
        return operations
