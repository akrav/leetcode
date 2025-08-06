class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=1:
            return x
        left = 0
        right = x
        res = 0

        while left < right:
            mid = left + (right - left)//2
            sqr = mid**2


            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
                res = mid
            else:
                right = mid
        
        return res

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         l, r = 0, x
#         res = 0

#         while l <= r:
#             m = l + (r - l) // 2
#             if m * m > x:
#                 r = m - 1
#             elif m * m < x:
#                 l = m + 1
#                 res = m
#             else:
#                 return m

#         return res