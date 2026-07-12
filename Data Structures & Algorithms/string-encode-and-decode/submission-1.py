class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            print(string)
            for ch in string:
                encoded += ch*2
            encoded += '010'
        print(encoded)

        return encoded


    def decode(self, s: str) -> List[str]:
        strs = []
        new_str = ""
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                new_str += s[i]
                i+=1
            if i > 0 and s[i-1] == '0' and s[i] == '1' and s[i+1] == '0':
                strs.append(new_str)
                new_str = ""
                i+=1
            i += 1
            
        return strs
