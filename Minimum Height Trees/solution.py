class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        q = []
        for key, value in adj_list.items():
            if len(value) == 1:
                q.append(key)

        count = 1
        while q:
            if n <= 2:
                return q
            leaves = len(q)

            for i in range(leaves):
                node = q.pop(0)
                n -= 1

                for neighbor in adj_list[node]:
                    adj_list[neighbor].remove(node)

                    if len(adj_list[neighbor]) == 1:
                        q.append(neighbor)
        return q