# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        total_chemistry = 0
        team = skill[left] + skill[right]
        
        while left < right:
            if (skill[left] + skill[right]) != team:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        return total_chemistry



        