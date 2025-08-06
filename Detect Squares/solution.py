class CountSquares:

    def __init__(self):
        self.point_dic = defaultdict(int)
        self.point_list = []
        

    def add(self, point: List[int]) -> None:
        self.point_dic[tuple(point)] += 1
        self.point_list.append(tuple(point))
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for point in self.point_list:
            x, y = point
            if x == px or y == py:
                continue
            if abs(px - x) != abs(py - y):
                continue
            
            res += self.point_dic[(px, y)] * self.point_dic[(x, py)]
        
        return res

        