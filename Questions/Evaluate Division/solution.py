class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            weight = values[i]
            adj_list[a].append([b, weight])
            adj_list[b].append([a, 1/weight])
        
        visited = {}
        def rec(src, target):
            if src not in adj_list or target not in adj_list:
                return -1
            if src == target:
                return 1
            
            visited[src] = True

            total = 1
            for neighor in adj_list[src]:
                next_node, weight = neighor
                if next_node not in visited:
                    val = rec(next_node, target)
                    if val != -1:
                        return val * weight 
            
            return -1
        

        ans = []
        for query in queries:
            visited = {}
            a, b = query
            ans.append(rec(a,b))
        return ans
        