class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        arr = [g - c for g, c in zip(gas, cost)]
        
        total = 0
        res = 0

        for i, diff in enumerate(arr):
            if total + diff > 0 and total == 0:
                total += diff
                res = i
            elif total + diff > 0:
                total += diff
            else:
                total = 0
        
        return res

    