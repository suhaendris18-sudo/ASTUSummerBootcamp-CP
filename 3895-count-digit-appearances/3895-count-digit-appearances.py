class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total_count = 0
        for num in nums:
            total_count += str(num).count(str(digit))
        return total_count    