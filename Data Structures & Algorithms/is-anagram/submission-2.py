class Solution:
   
    def isAnagram(self, s: str, t: str) -> bool:
       char=[0]*26
       for i in s:
        #a=97,z=122
        char[ord(i)-97] +=1
       for i in t:
        #a=97,z=122
        char[ord(i)-97] -=1
       for count in char:
            if count!=0:
                return False
       return True
