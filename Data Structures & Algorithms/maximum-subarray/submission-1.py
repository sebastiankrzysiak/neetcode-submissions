class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        total = 0

        largest = max(nums)
        if largest < 0:
            return largest

        for num in nums:
            if num + total > 0:
                total += num
                res = max(res, total)
            else:
                total = 0
                res = max(res, total)
        
        return res