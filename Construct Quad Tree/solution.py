"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row_origin, col_origin, side_len):
            val = grid[row_origin][col_origin]

            if is_single_value(row_origin, col_origin, side_len):
                return Node(val = val, isLeaf = True)
            
            root = Node(val = 0, isLeaf = False)
            tl, tr, bl, br = get_new_origin_points(row_origin, col_origin, side_len)

            root.topLeft = helper(tl[0], tl[1], side_len//2)
            root.topRight = helper(tr[0], tr[1], side_len//2)
            root.bottomLeft = helper(bl[0], bl[1], side_len//2)
            root.bottomRight = helper(br[0], br[1], side_len//2)

            return root
                
        
        def is_single_value(row_origin, col_origin, side_len):
            count = 0
            for i in range(row_origin, row_origin + side_len):
                for j in range(col_origin, col_origin + side_len):
                    count += grid[i][j]

            return True if (count == 0) or (count == side_len**2) else False

        def get_new_origin_points(row_origin, col_origin, side_len):
            half_side_len = side_len // 2

            top_left = (row_origin, col_origin)
            top_right = (row_origin, col_origin + half_side_len)
            bottom_left = (row_origin + half_side_len, col_origin)
            bottom_right = (row_origin + half_side_len, col_origin + half_side_len)
            return  (top_left, top_right, bottom_left, bottom_right)
        
        return helper(0, 0, len(grid))