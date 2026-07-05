class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def visit(i):
            total = sum(cur)
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            visit(i)
            cur.pop()
            visit(i + 1)

        visit(0)
        return res