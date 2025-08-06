class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        store = [-1000000,-1000000,-1000000]

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            store = [max(store[0], a),\
                     max(store[1], b),
                     max(store[2], c)
                    ]
            print(store)
        return store == target

            

        