class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def helper(i , j ) -> int:
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return 0
            if grid[i][j] == "1":
                grid[i][j] = "0"
                return (1 + helper(i+1,j) + helper(i-1,j) + helper(i, j+1) + helper(i , j-1))
            else:
                return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    helper(i , j)

        return count
                
    


    

               
        