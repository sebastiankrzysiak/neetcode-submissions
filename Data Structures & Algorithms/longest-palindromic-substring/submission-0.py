class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = None
        end = None
        length = 0

        def palindrome(l, r):
            nonlocal start, end, length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > length):
                    length = r - 1 + 1
                    start = l
                    end = r + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i + 1)
        
        return s[start:end]