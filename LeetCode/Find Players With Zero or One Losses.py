class Solution(object):
    def findWinners(self, matches):
        from collections import defaultdict
        
        wins = defaultdict(int)
        losses = defaultdict(int)
        
        for winner, loser in matches:
            wins[winner] += 1
            losses[loser] += 1
        
        no_losses = []
        one_loss = []
        
        all_players = set(wins.keys()).union(set(losses.keys()))
        
        for player in all_players:
            if losses[player] == 0:
                no_losses.append(player)
            elif losses[player] == 1:
                one_loss.append(player)
        
        return [sorted(no_losses), sorted(one_loss)]

