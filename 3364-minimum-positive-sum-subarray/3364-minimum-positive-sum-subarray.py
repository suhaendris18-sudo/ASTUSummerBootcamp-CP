class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ms = []
        for i in range(l, r+1):
            window_sum= sum(nums[:i])
            if window_sum > 0:
                ms.append(window_sum)
            for j in range(i, len(nums)):
                window_sum = window_sum + nums[j] - nums[j-i]
                if window_sum> 0:
                    ms.append(window_sum)
        if not ms:
            return -1
        return min(ms)
        




#         [3, -2, 1, 4], l = 2, r = 3
#         for i in range(l, r+1) = i=2 and i=3

#         window_sum= sum(nums[:i]) =nums[:2] = [3, -2] ws=1

#         if ws > 0 =list append(ws)  ms[1]


#          for j in range(i, len(nums))
#          i=2  (2,4)  j=2 and j=3
        

#         j=2  [3, -2] => [-2,1]
#         window_sum = window_sum + nums[j] - nums[j-i]
#         ws= 1+nums[2] - nums[0]
#         1+1-3 =-1

#         if ws > 0=ms.append ws
#         -1<0    => ms[1]
# j=3
# [1 4]
# ws=-1+nums[3]-nums[1]
# -1+4-(-2)=5
# 5 is postive ms=[1,5]

# i=3
# [3,-2,1]
# ws=2 its postuve ms[1,5,2]

# j=3
# [-2,1,4]
# ws=2+nums[3]-nums[0]
# 2+4-3 =3 
# ms[1,5,2,3]

# if notms = print-1
# printmin(ms)