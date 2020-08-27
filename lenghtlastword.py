class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) > 0:            
            slist = s.split(' ')        
            last = slist[len(slist) - 1]            
            return len(last)
        else: 
            return 0
