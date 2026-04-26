class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = 0

        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        
        queue = deque([node for node in range(numCourses) if node not in indegrees])

        while queue:
            node = queue.popleft()
            seen += 1
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        return seen == numCourses