class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [(-cnt, task) for task, cnt in count.items()]
        heapq.heapify(heap)
        time = 0

        while heap:
            history = []
            for _ in range(n + 1):
                if heap:
                    cnt, task = heapq.heappop(heap)
                    cnt += 1
                    if cnt != 0:
                        history.append((cnt, task))
                    time += 1
                elif history:
                    time += 1
            
            for cnt, task in history:
                heapq.heappush(heap,(cnt, task))
        
        return time