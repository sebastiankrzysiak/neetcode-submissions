class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)]

        print(count)

        for num, cnt in freq.items():
            count[cnt].append(num)
        
        res = []

        for i in range(len(count) -1, -1, -1):
            arr = count[i]
            if arr:
                for num in arr:
                    res.append(num)
                    k -= 1
                    if not k:
                        return res
        
        return res
