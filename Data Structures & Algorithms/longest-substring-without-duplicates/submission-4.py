class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        r = 0

        while r < len(s):
            can_grow = s[r] not in seen
            if can_grow:
                seen.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                seen.remove(s[l])
                l += 1
        
        return res