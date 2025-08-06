class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combo = []

        for p, s in zip(position, speed):
            combo.append((p,s))

        combo.sort(reverse = True)
        print(combo)

        stack = [(target-combo[0][0])/combo[0][1]]

        count = 1
        for i in range(1,len(combo)):
            time_to_target = (target-combo[i][0])/combo[i][1]
            if time_to_target > stack[-1]:
                count+=1
                stack.append(time_to_target)

        print(stack)
        return count