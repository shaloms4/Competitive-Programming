class Solution(object):
    def interpret(self, command):
        goal_parser_interpretation = []
        i = 0
        while i < len(command):
            if i + 3 < len(command) and command[i:i + 4] == '(al)':
                goal_parser_interpretation.append('al')
                i +=4
            elif i + 1 < len(command) and command[i:i + 2] == '()':
                goal_parser_interpretation.append('o')
                i +=2
            elif command[i] == 'G':
                goal_parser_interpretation.append('G')
                i +=1
        return ''.join(goal_parser_interpretation)

solution=Solution()