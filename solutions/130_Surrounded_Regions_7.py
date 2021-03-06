class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        m = len(board)
        if m <= 2:
            return 
        n = len(board[0])
        if n <= 2:
            return 
        for ix in (0, m-1):
            for jx in (0, n-1):
                if board[ix][jx] == \u0027O\u0027:
                    self.flip(ix, jx, board, m, n)
        for ix in range(m):
            for jx in range(n):
                if board[ix][jx] == \u0027O\u0027:
                    board[ix][jx] = \u0027X\u0027
                elif board[ix][jx] == \u00271\u0027:
                    board[ix][jx] = \u0027O\u0027
    def flip(self, ix, jx, board, m, n):
        if not 0<=ix<m or not 0<=jx <n:
            return 
        if board[ix][jx] == \u0027O\u0027:
            board[ix][jx] =\u00271\u0027
            self.flip(ix -1, jx, board, m, n)
            self.flip(ix+1, jx, board, m, n)
            self.flip(ix, jx-1, board, m, n)
            self.flip(ix, jx+1, board, m, n)
            
                