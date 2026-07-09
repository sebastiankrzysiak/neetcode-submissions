class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for w in words for c in w}
        indegree = {c : 0 for c in graph}

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] == w2[j]:
                    continue
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
      
        
        queue = deque(letter for letter in graph if indegree[letter] == 0)
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return "".join(res) if len(res) == len(graph) else ""
        