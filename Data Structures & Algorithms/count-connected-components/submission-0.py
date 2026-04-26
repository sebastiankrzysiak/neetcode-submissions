class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def visit(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    visit(nei)
        
        count = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                visit(node)
                count += 1
        
        return count
