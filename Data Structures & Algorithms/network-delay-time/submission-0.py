class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, wei in times:
            graph[u].append((wei, v))
        
        pq = [(0, k)]
        distances = {k:0}

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > distances[node]:
                continue

            for wei, nei in graph[node]:
                if nei not in distances or cost + wei < distances[nei]:
                    distances[nei] = cost + wei
                    heapq.heappush(pq, (distances[nei], nei))
        
        return max(distances.values()) if len(distances) == n else -1