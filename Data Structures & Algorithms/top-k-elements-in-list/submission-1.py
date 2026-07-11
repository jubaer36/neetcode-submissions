class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num,0) + 1
        elements = [key for key,value in (sorted(res.items(), key=lambda x:x[1], reverse=True))]
        
        elements = elements[:k]
        print(res)              
        return elements
        