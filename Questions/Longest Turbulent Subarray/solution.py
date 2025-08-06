# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         if len(arr) == 1:
#             return 1

#         for i in range(len(arr)-1):
#             arr[i] = arr[i+1] - arr[i]
        
#         max_count = 1 if sum(arr[:-1]) != 0 else 0
#         count = 1
#         for i in range(len(arr)-2):
            
#             if arr[i] == 0 or arr[i+1] == 0:
#                 count = 1
#                 continue

#             if arr[i]/abs(arr[i]) != arr[i+1]/abs(arr[i+1]):
#                 count += 1
#             else:
#                 count = 1
            
#             max_count = max(max_count, count)
#         return 1 if max_count == 0 else max_count + 1


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res