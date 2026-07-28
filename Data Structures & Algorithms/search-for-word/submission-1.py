class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        col , row = len(board[0]) , len(board)
        it = 0
        def helper(i , j , it):
            if it == len(word):
                return True
            
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j]!=word[it]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            found = helper(i+1,j,it+1) or helper(i-1,j,it+1) or helper(i,j+1,it+1) or helper(i,j-1,it+1)           
            board[i][j] = temp
            return found
        ans = False              
        for i in range(row):
                for j in range(col):
                    ans = ans or helper(i , j , it)
        
        
        return ans
        