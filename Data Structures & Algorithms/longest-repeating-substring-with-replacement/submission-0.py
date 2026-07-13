class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq_map = {}
        max_freq = 0
        window_size = 0
        ans = 0
        max_window_size = 0

        for right in range(len(s)):
            freq = freq_map.get(s[right],0) + 1
            freq_map[s[right]] = freq
            max_freq = max(max_freq , freq)
            window_size = right - left + 1
            while window_size - max_freq > k:
                freq_map[s[left]] -=  1
                left += 1
                window_size = right - left + 1
            
            ans = max(window_size , ans)

            

        return ans
            

        