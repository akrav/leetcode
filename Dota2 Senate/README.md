[Back to Table of Contents](../README.md)

# Dota2 Senate
Difficulty: Medium

## Question
Dota2 Senate
Solved
Medium
Topics
premium lock icon
Companies
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.

## Solution Template
```python
# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         party_count = defaultdict(int)

#         for party in senate:
#             party_count[party] += 1
        
#         D_to_remove = 0
#         R_to_remove = 0
#         for party in senate:
#             if party == 'D' and D_to_remove > 0:
#                 D_to_remove -= 1
#                 continue
#             if party == 'R' and R_to_remove > 0:
#                 R_to_remove -= 1
#                 continue

#             if party == 'R':
#                 party_count['D'] -= 1
#                 D_to_remove += 1
#             else:
#                 party_count['R'] -= 1
#                 R_to_remove += 1
            
#             if party_count['R'] == 0:
#                 return 'Dire'
#             if party_count['D'] == 0:
#                 return 'Radiant'
#         if party_count['R'] == party_count['D']:
#             return 'Radiant' if senate[-1] == 'R' else 'Dire'
#         return 'Radiant' if max(party_count, key=party_count.get) == 'R' else 'Dire'


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + n)
            else:
                D.append(dTurn + n)

        return "Radiant" if R else "Dire"
```
