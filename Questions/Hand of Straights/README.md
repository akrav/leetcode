[Back to Table of Contents](../../README.md)

# Hand of Straights
Difficulty: Medium

## Question
Hand of Straights
Solved 
You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.

Example 1:

Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

Example 2:

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.

Constraints:

1 <= hand.length <= 1000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length

## Solution Template
```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hands = [[hand[0]]]
        for i in range(1, len(hand)):
            added = False
            for fan in hands:
                if added == True:
                    continue
                if len(fan) == groupSize:
                    continue
                if hand[i] == fan[-1] + 1:
                    fan.append(hand[i])
                    added = True
            
            if added == False:
                hands.append([hand[i]])
        
        for fan in hands:
            if len(fan) != groupSize:
                return False
        
        return True
                


        
```
