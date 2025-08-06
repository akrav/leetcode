import heapq as hq
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         for i in range(len(trips)):
#             trips[i][0], trips[i][1], trips[i][2] = trips[i][1], trips[i][2], trips[i][0]
#         # enque, de_que, capacity

#         trips.sort(key=lambda t: t[0])
#         minHeap = []
#         i = 0
#         location = trips[0][0]
#         curr_capacity = 0
#         while minHeap or i < len(trips):
#             while i < len(trips) and location <= trips[i][0]:
#                 heapq.heappush(minHeap, [trips[i][1], trips[i][2]])
#                 curr_capacity += trips[i][2]
#                 i += 1
#             if not minHeap:
#                 location = trips[i][0]
#                 curr_capacity += trips[i][2]
#                 # if curr_capacity > capacity:
#                 #     return False
#             else:
#                 drop_off, car_capacity = heapq.heappop(minHeap)
#                 curr_capacity -= car_capacity
#                 location =  drop_off
            
#             if  curr_capacity > capacity:
#                     return False
                
#         return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        
        minHeap = []  # pair of [end, numPassengers]
        curPass = 0
        
        for numPass, start, end in trips: 
                              # If the end of the smallest end trip is less than our current location
                              # that means we can remove passengers
            while minHeap and minHeap[0][0] <= start:
                curPass -= hq.heappop(minHeap)[1]
            
            # Now we need to add our passengers to the road and we need to
            # push to the heap to see when they get off the road
            
            curPass += numPass
            if curPass > capacity:
                return False
            
            hq.heappush(minHeap, [end, numPass])
        
        return True
    