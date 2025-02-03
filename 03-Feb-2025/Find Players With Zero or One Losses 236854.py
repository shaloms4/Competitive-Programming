# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loser = defaultdict(int)
        for nums in matches:
            winner[nums[0]] += 1
            loser[nums[1]] += 1
        win = []
        loss = []
        for i in winner.keys():
            if i not in loser:
                win.append(i)
         
        for j in loser.keys():
            if loser[j] == 1:
                loss.append(j)
        return [sorted(win), sorted(loss)]

        