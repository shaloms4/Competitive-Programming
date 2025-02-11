# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        count = 0 
        while count < 4:
            output = []
            for j in range(len(mat[0])): 
                temp = []
                for i in range(len(mat) - 1, -1, -1):  
                    temp.append(mat[i][j])
                output.append(temp)
            mat = output 
            if output == target:
                return True
             
            count += 1
            
        return False


        
        