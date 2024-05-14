class Solution(object):
    def isPalindrome(self, x):
        string_x=str(x)
        start=0
        end=len(string_x)-1
        while start<end:
            if string_x[start]!=string_x[end]:
                return False
            start+=1
            end-=1
        return  True


        
        