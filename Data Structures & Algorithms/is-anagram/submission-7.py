class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mem = [0]*26
        for i in range(len(s)):
            mem[ord(s[i]) - ord('a')] +=1
            mem[ord(t[i]) - ord('a')] -=1
        for i in mem:
            if i !=0:
                return False
        return True

