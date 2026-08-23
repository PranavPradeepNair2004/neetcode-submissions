class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through each element
        for i in range(len(nums)):
            # Loop through the remaining elements after 'i'
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] # Return the indices as a list