class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = sum(nums[0 : k])
        max_sum = window_sum

       # n = len(nums)
        for i in range (k,len(nums)):

           # left = i - k
            #right = i
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum , window_sum)
            #for j in range(i, i + k):
               # window_sum += nums[j]
           # max_sum = max(max_sum, window_sum)
        return max_sum / k       