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
                


        