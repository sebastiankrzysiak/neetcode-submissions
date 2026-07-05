class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()

        def visit(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            visit(i + 1)
            cur.pop()
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
            visit(i)
            
        visit(0)
        return res