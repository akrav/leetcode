[Back to Table of Contents](../README.md)

# Minimum Stack
Difficulty: Medium

## Question
Minimum Stack
Solved 
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.

## Solution Template
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele_idx = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_ele_idx == []:
            self.min_ele_idx.append(len(self.stack)-1)
        else:
            curr_min_idx = self.min_ele_idx[-1]
            curr_min_val = self.stack[curr_min_idx]

            if curr_min_val >= val:
                self.min_ele_idx.append(len(self.stack)-1)
            else:
                self.min_ele_idx.append(curr_min_idx)




    def pop(self) -> None:
        n = len(self.stack)
        if n > 0:
            
            self.min_ele_idx.pop()
            self.stack.pop()
        
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        curr_min_idx = self.min_ele_idx[-1]
        curr_min_val = self.stack[curr_min_idx]
        return curr_min_val
        
```
