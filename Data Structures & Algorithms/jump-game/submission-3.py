class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1 , -1 , -1):
            if goal == 0:
                return True
            if nums[i] + i >= goal:
                goal = i
                i = goal - 1
            
        if goal == 0:
            return True
        return False
            

        