class Solution:
    def balancedString(self, s: str) -> int:
        
        n = len(s)
        left = 0
        ans = n
        counter = Counter(s) 
        
        for right in range(n):
            counter[s[right]] -= 1

            while left < n and 4*max(counter.values()) <= n:
                ans = min(ans, right-left+1) 
                counter[s[left]] += 1 
                left += 1

        return ans

        
        