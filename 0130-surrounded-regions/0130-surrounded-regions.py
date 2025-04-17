class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
       
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[len(board)-1][j] == 'O':
                dfs(len(board)-1, j)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][len(board[0])-1] == 'O':
                dfs(i, len(board[0])-1)
        
       
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
