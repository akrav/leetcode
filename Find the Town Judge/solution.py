class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n <= 1:
            return 1
        possible_ans = []
        trust_dic = defaultdict(list)
        reverse_trust_dic = defaultdict(list)
        for person, person_of_trust in trust:
            trust_dic[person_of_trust].append(person)
            reverse_trust_dic[person].append(person_of_trust)
            if len(trust_dic[person_of_trust]) == n-1:
                possible_ans.append(person_of_trust)
        
        for possible_judge in possible_ans:
            if len(reverse_trust_dic[possible_judge]) == 0:
                return possible_judge

        return -1