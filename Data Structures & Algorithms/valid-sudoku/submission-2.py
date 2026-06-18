class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            unique_nums_row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in unique_nums_row:
                    unique_nums_row.add(board[i][j])
                else:
                    return False

        for i in range(9):
            unique_nums_col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] not in unique_nums_col:
                    unique_nums_col.add(board[j][i])
                else:
                    return False
        
        unique_nums_square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in unique_nums_square[tuple([i//3, j//3])]:
                    unique_nums_square[tuple([i//3, j//3])].add(board[i][j])
                else:
                    return False

        return True