class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def is_before(i):
            return nums[i] < target
        
        if nums[l] == target:
            return l
        
        while r - l > 1:
            m = (l + r) // 2
            if is_before(m):
                l = m
            else:
                r = m
        
        return r if nums[r] == target else -1