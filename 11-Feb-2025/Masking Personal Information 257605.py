# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            masked_email = []
            idx = s.index("@")
            for i in range(len(s)):
                if i >= idx-1 or i == 0:
                    masked_email.append(s[i].lower())
            masked_email.insert(1, "*****") 
            return ''.join(masked_email)       
        else:
            separation = {'+', '-', '(', ')', ' '}
            no_separation_phone = []
            for i in range(len(s)):
                if s[i] in separation:
                    pass
                else:
                    no_separation_phone.append(s[i])
            masked_phone = []
            if len(no_separation_phone) == 10:
                masked_phone.append("***-***-")
            elif len(no_separation_phone) == 11:
                masked_phone.append("+*-***-***-")
            elif len(no_separation_phone) == 12:
                masked_phone.append("+**-***-***-")
            elif len(no_separation_phone) == 13:
                masked_phone.append("+***-***-***-")
            for i in range(len(no_separation_phone) - 4, len(no_separation_phone)):
                masked_phone.append(no_separation_phone[i])
            return ''.join(masked_phone)

        

       
        
       

        
            
        