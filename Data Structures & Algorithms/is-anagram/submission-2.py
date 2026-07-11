class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}

        for char in s:
            counter[char] = counter.get(char,0) + 1
        for char in t:
            if char not in counter:
                return False
            current_count = counter.get(char)
            if current_count <= 0:
                return False
            counter[char] =  current_count - 1
        return True

        

        
        
        