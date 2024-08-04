class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        left = 0
        right = n - 1
        target_sum = skill[left] + skill[right]
        
        total_chemistry = 0
        
        while left < right:
            team_sum = skill[left] + skill[right]
            if team_sum != target_sum:
                return -1
            
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total_chemistry
            