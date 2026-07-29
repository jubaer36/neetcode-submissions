class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums2 = nums[1:]
        nums1 = nums[:-1]
        memo = {}
        def findMax(curIdx , numbers):
            if curIdx in memo:
                return memo[curIdx]
            if curIdx >= len(numbers):
                return 0
            memo[curIdx] =  max(numbers[curIdx]+ findMax(curIdx + 2 , numbers) , findMax(curIdx + 1, numbers))
            return memo[curIdx]
            
        v1 = findMax(0,nums1.copy())
        memo = {}
        v2 = findMax(0,nums2.copy())
        return max(v1,v2)

            

        