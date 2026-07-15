
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        let1={}
        let2={}
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            let1[s[i]]=let1.get(s[i], 0) + 1
            let2[t[i]]=let2.get(t[i], 0) + 1
        if let1 == let2:
            return True
        return False