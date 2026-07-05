class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        

        def visit(i):
            total = sum(cur)
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            visit(i + 1)
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
              i += 1
            cur.pop()
            visit(i)

        visit(0)
        return res