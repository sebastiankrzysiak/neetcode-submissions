class Solution:
    def findMin(self, nums: List[int]) -> int:
        def is_before(i):
            return nums[0] < nums[i]

        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        while r - l > 1:
            m = (l + r) // 2
            if is_before(m):
                l = m
            else:
                r = m
        
        return nums[r]