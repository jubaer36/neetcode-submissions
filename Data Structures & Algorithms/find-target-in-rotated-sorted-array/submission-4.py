class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        print(f"Pivot: {l}")
        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0

        

        while l <= r:
            mid = l + (r-l)//2
            print(f"Left: {l} ,Mid: {mid}, Right: {r}")
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1



        