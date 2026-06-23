class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n= len(prices)
        left=1
        count=1
        for i in range( 1,n):
            if prices[i] == prices[i-1]-1:
                count +=1
            else:
                count = 1
            left += count
        return left        



        