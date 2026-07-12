class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        stack = []
        print(s)
        for i in range(len(s)//2):
            if s[i].isalnum():
                stack.append(s[i].lower())
        
        start = len(s)//2 if len(s)%2==0 else len(s)//2 + 1
        
        for i in range(start, len(s)):
            if s[i].isalnum():
                if stack.pop() != s[i].lower():
                    return False

        
        return True

        