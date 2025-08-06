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
        