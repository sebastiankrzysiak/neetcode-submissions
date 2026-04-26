class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def visit(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    visit(nei)
        
        visited.add(0)
        visit(0)

        return len(edges) == n - 1 and len(visited) == n