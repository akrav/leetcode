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