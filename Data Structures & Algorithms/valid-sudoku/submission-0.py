class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in row_sets[i] or val in col_sets[j] or val in box_sets[(i//3)*3 + (j//3)]:
                    return False
                row_sets[i].add(val)
                col_sets[j].add(val)
                box_sets[(i//3)*3 + j//3].add(val)
        
        return True



            


        