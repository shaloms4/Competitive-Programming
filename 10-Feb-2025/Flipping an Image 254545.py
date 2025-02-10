# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        flip = []
        for i in range(row):
            image[i].reverse()
            flip.append(image[i])
        invert = []
        for nums in flip:
            temp = []
            for i in range(col):
                if nums[i] == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            invert.append(temp)
        return invert


        