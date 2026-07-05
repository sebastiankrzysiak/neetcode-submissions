class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def visit(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            visit(i + 1)
            cur.pop()
            visit(i + 1)
        
        visit(0)
        return res