class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = {}
        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums[num] = True

        return False




        