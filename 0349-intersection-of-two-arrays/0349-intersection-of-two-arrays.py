class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=set(nums1)
        temp=set()
        for n in nums2:
            if n  in k :
                temp.add(n)
        return list(temp)        