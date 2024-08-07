class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pointer_1 = 0
        pointer_2 = 0
        count = 0
        while pointer_1 < len(players) and pointer_2 < len(trainers):
            if players[pointer_1] <= trainers[pointer_2]:
                pointer_1 += 1
                pointer_2 += 1
                count += 1
            else: 
                pointer_2 += 1
        return count
