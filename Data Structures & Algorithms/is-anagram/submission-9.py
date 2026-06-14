class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memory = [0]*26
        for element in range(len(s)):
            memory[ord(s[element])-ord('a')]+=1
            memory[ord(t[element])-ord('a')]-=1
        for i in memory:
            if i !=0 :
                return False
        return True

