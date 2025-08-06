import heapq as hq
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        
    def binary_search_convergence(self, li, timestamp: int) -> int:
        left = 0
        right = len(li)-1
        mid = 0
        while left < right:
            mid = left + math.ceil((right-left) / 2)
            ts, val = li[mid]
            
            if ts > timestamp:
                right = mid -1
            elif ts < timestamp:
                left = mid
            else:
                return mid

        return right
    
    def binary_search_classic(self, li, timestamp: int) -> int:
        left = 0
        right = len(li)-1
        mid = 0
        while left <= right:
            mid = left + (right-left) // 2
            ts, val = li[mid]
            
            if ts > timestamp:
                right = mid -1
            elif ts < timestamp:
                left = mid + 1
            else:
                 return mid

        return right

    def get(self, key: str, timestamp: int) -> str:
        if self.dic[key] == []:
            return ""
        idx = self.binary_search_classic(self.dic[key], timestamp)
        print(f"idx: {idx}")
        ts, val = self.dic[key][idx]
        if ts <= timestamp:
            return val
        return ""
        