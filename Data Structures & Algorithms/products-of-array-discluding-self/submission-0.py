class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None]* len(nums)
        prefix = []
        suffix = []
        
        
        for i in range(len(nums)):
            if len(prefix) < 1:
                prefix.append(nums[0])
            else:
                prefix.append(prefix[-1]*nums[i])
            if len(suffix) < 1:
                suffix.append(nums[-1])
            else:
                suffix.append(suffix[-1]*nums[-i-1])
            
        print(prefix)
        
        suffix.reverse()
        print(suffix)
        for i in range(1,len(nums)-1):
            output[i] = prefix[i-1]*suffix[i+1]
        
        output[0] = suffix[1]
        output[-1] = prefix[-2]

        return output
        

        