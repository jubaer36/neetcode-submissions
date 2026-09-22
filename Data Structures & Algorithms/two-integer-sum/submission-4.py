class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        it = 0
        ans = []
        for num in nums:
            complement = target - num
            if complement in pos:
                ans.append(pos[complement])
                ans.append(it)
            pos[num] = it
            it+=1
        return ans

        