class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for num in sett:
            length = 0
            if num - 1 not in sett:
                length += 1
                while num + length in sett:
                    length += 1
            res = max(res, length)
        return res
