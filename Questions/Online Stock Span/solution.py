# class StockSpanner:

#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#         self.memo = {}
        

#     def next(self, price: int) -> int:
#         count = 1
        
#         while self.stack1 and self.stack1[-1] <= price:
#             self.stack2.append(self.stack1.pop())
#             count += 1
        
#         for i in range(len(self.stack2)):
#             self.stack1.append(self.stack2.pop())
#         self.stack1.append(price)

#         self.memo[len(self.stack1)] = count
            
#         return count


# class StockSpanner:

#     def __init__(self):
#         self.stack1 = []
#         self.memo = []
        

#     def next(self, price: int) -> int:
#         count = 1
        
#         if len(self.stack1) == 0 or self.stack1[-1] > price:
#             self.stack1.append(price)
#             return count
        
        
#         for i in range(1, len(self.stack1)+1):
#             if (len(self.stack1)-i) < 0 or (self.stack1[len(self.stack1)-i] > price):
#                 self.stack1.append(price)
#                 return count

#             count += 1
#         self.stack1.append(price)
#         return count
        
#neetcode solution
# The trick is if you pop a value you never need to look at it again you only need to look at the potential next biggest value which is why a stack works
class StockSpanner:

    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)