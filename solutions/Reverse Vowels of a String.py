class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)
        pointer_1 = 0
        pointer_2 = len(s) - 1
        
        while pointer_1 < pointer_2:
            while pointer_1 < pointer_2 and s[pointer_1] not in vowels:
                pointer_1 += 1
            while pointer_1 < pointer_2 and s[pointer_2] not in vowels:
                pointer_2 -= 1

            if pointer_1 < pointer_2:
                s[pointer_1], s[pointer_2] = s[pointer_2], s[pointer_1]
                pointer_1 += 1
                pointer_2 -= 1
        
        return ''.join(s)


