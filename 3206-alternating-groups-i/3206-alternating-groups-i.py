class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        new_arr=colors+colors[:2]
        count=0
        for i in range(len(colors)):
             if new_arr[i]!=new_arr[i+1] and new_arr[i]==new_arr[i+2]:
                count+=1
        return count
        