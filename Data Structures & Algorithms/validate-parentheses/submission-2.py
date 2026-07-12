class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2:
            return False
        i = 0
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(')')
            elif s[i] =='{':
                stack.append('}')
            elif s[i] =='[':
                stack.append(']')
            else:
                if not stack or s[i] != stack.pop():
                    return False
                

        return not stack
        