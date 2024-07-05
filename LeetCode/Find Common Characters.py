class Solution(object):
    def commonChars(self, words):
        if not words:
            return []
        
        common_characters = {}
        for char in words[0]:
            common_characters[char] = common_characters.get(char, 0) + 1
        
        for word in words[1:]:
            current_count = {}
            for char in word:
                current_count[char] = current_count.get(char, 0) + 1
            
            for char in common_characters.keys():
                if char in current_count:
                    common_characters[char] = min(common_characters[char], current_count[char])
                else:
                    common_characters[char] = 0
        
        result = []
        for char, count in common_characters.items():
            result.extend([char] * count)
        
        return result