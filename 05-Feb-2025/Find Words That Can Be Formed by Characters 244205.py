# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = Counter(chars)
        count = 0
        for word in words: 
            
            count_word = Counter(word)
            for key, value in count_word.items():
                if key not in count_chars or value > count_chars[key]:
                    break
            else:
                count += len(word)
                    
        return count

        