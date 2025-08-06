[Back to Table of Contents](../../README.md)

# Car Pooling
Difficulty: Medium

## Question
Car Pooling
Solved
Medium
Topics
premium lock icon
Companies
Hint
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105

## Solution Template
```python
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
    
```
