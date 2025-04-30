class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ret = []
        graph = {}

        def dfs(dst, path):
            if path[-1] not in graph:
                return -1.0

            if path[-1] == dst:
                return 1.0

            for n, w in graph[path[-1]]:
                if n not in path:
                    path.append(n)
                    val = dfs(dst, path)
                    path.pop()

                    if val != -1.0:
                        return val * w * 1.0
            return -1.0

        for i in range(len(equations)):
            a, b = equations[i]
            if b not in graph:
                graph[b] = []
            if a not in graph:
                graph[a] = []
            graph[b].append((a, values[i]))
            graph[a].append((b, 1.0 / values[i]))

        for c, d in queries:
            ret.append(dfs(c, [d]))

        return ret
