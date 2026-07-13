class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substr_length = 0
        ans = 0
        ascii_map = {}
        while right < len(s):
            if s[right] not in ascii_map:
                substr_length += 1
                ascii_map[s[right]]=1
                right+=1
                ans = max ( ans , substr_length)
            else:
                substr_length = 0
                left += 1
                right = left
                ascii_map = {}
        return ans
            
