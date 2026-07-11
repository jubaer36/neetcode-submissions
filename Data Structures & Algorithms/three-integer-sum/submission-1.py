class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        it = 0
        print(nums)
        for cur in nums:
            if it > 0 and nums[it] == nums[it-1]:
                it += 1
                continue
            cur = cur * (-1)
            left_pt = it + 1
            right_pt = len(nums) - 1
            while left_pt < right_pt:
                if it != left_pt and it != right_pt:
                    two_sum = 1*(nums[left_pt] + nums[right_pt])
                    if cur == two_sum:
                        print(cur , two_sum)
                        ans.append([nums[it], nums[left_pt], nums[right_pt]])
                        left_pt += 1
                        right_pt -= 1
                        while left_pt < right_pt and nums[left_pt] == nums[left_pt - 1]:
                            left_pt += 1
                        while left_pt < right_pt and nums[right_pt] == nums[right_pt + 1]:
                            right_pt -= 1
                    elif cur < two_sum:
                        right_pt -= 1
                    else:
                        left_pt += 1
                elif it == left_pt:
                    left_pt += 1
                elif it == right_pt:
                    right_pt -= 1
                
            it+=1
            
        return ans


            




            

        

        return []
        
        