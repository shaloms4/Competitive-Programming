class Solution(object):
    def similarPairs(self, words):
        char_set_count = {}

        for word in words:
            char_set = ''.join(sorted(set(word)))
            if char_set in char_set_count:
                char_set_count[char_set] += 1
            else:
                char_set_count[char_set] = 1
        pairs = 0
        for count in char_set_count.values():
            if count > 1:
                pairs += count * (count - 1) // 2
        return pairs



        