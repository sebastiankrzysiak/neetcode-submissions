class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house(i, nums, memo):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + house(i + 2, nums, memo), house(i + 1, nums, memo))

            return memo[i]

        return max(house(0, nums[1:], {}), house(0, nums[:-1], {}))