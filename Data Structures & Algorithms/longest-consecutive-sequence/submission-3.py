class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        print(numset)
        ans = 0
        for num in numset:
            if num - 1 not in numset:
                length =  1
                curr = num
                while curr + 1 in numset:
                    print(curr)
                    length += 1                
                    curr = curr + 1
                ans = max (ans , length)


        return ans
                

        