class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def climb(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(cost[i] + climb(i + 1), cost[i] + climb(i + 2))
            
            return memo[i]
        
        return min(climb(0), climb(1))