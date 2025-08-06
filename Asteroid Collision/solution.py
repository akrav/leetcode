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
        