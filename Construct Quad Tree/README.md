[Back to Table of Contents](../README.md)

# Construct Quad Tree
Difficulty: Medium

## Question
Construct Quad Tree
Solved
Medium
Topics
premium lock icon
Companies
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6

## Solution Template
```python
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
```
