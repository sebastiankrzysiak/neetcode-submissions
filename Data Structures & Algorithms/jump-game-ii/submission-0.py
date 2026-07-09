class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        
        def game(i):
            if i == len(nums) - 1:
                return 0
            if i > len(nums) - 1:
                return float("inf")
            if i in memo:
                return memo[i]
            
            jumps = float("inf")
            for length in range(1, nums[i] + 1):
                jumps = min(jumps, 1 + game(i + length))
            
            memo[i] = jumps
            return memo[i]
        
        return game(0)