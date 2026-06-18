class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        max_length = 0
        for i in range(len(nums)):
            while nums[i] - nums[left] > 1:
                left += 1
            if nums[i] - nums[left] == 1:
                max_length = max(max_length, i - left + 1)    
 
        return max_length