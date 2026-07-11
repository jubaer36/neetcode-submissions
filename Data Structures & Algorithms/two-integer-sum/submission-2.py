class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        it = 0
        ans = []
        for x in nums:
            complement = target - x
            if complement in pos:
                ans.append(pos[target - x])
                ans.append(it)
                return ans
            pos[x] = it
            it+=1
            

        return ans

        