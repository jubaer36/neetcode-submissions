
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(curList, total , start):
            if total == target:
                res.append(curList[:])

            for i in range(start , len(candidates)):
                if total > target or i >= len(candidates):
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                curList.append(candidates[i])
                helper(curList, total+candidates[i] , i + 1)
                curList.pop()
        
        helper([],0,0)

        return res

            
            
                
            

            
        
        