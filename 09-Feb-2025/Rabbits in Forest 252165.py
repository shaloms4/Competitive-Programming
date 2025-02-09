# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer = 0
        count_answers = Counter(answers)
        
        for key, value in count_answers.items():
            groups = (value + key) // (key + 1)
            answer += groups * (key + 1)
            
        return answer
