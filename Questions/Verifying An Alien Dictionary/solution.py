class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = 1
        letter_order = {}
        for letter in order:
            letter_order[letter] = count
            count += 1
        

        for i in range(1, len(words)):
            word_1 = words[i-1]
            word_2 = words[i]
            same_beginning = True
            for j in range(min(len(word_1), len(word_2))):
                same_beginning = same_beginning and (word_1[j] == word_2[j])
                print(f"j: {j}, word_1[j]: {word_1[j]}, word_2[j]: {word_2[j]}")
                if letter_order[word_1[j]] < letter_order[word_2[j]]:
                    break
                elif letter_order[word_1[j]] > letter_order[word_2[j]]:
                    return False

            if same_beginning and len(word_1) > len(word_2):
                return False
                
        return True
        