class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def house(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + house(i + 2), house(i + 1))

            return memo[i]
        
        return house(0)