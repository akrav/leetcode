[Back to Table of Contents](../../README.md)

# Asteroid Collision
Difficulty: Medium

## Question
Asteroid Collision
Solved
Medium
Topics
premium lock icon
Companies
Hint
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

## Solution Template
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            if len(stack) == 0:
                stack.append(asteroids[i])
                continue
            meteor1 = stack.pop()
            meteor2 = asteroids[i]

            if meteor1 > 0 and meteor2 < 0:
                if abs(meteor2) > abs(meteor1):
                    remaining_meteor = meteor2
                elif abs(meteor2) < abs(meteor1):
                    remaining_meteor = meteor1
                else:
                    remaining_meteor = 0

                while remaining_meteor < 0 and len(stack) != 0 and stack[-1] > 0:
                    meteor3 = stack.pop()
                    if abs(remaining_meteor) > abs(meteor3):
                        remaining_meteor = remaining_meteor
                    elif abs(remaining_meteor) < abs(meteor3):
                        remaining_meteor = meteor3
                    else: 
                        remaining_meteor = 0

                if remaining_meteor != 0:
                    stack.append(remaining_meteor)
            else:
                stack.append(meteor1)
                stack.append(meteor2)
        
        return stack
        
```
