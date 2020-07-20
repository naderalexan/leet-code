class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def flip_adjacent(b, i, j):
            try:
                cur = b[i][j]
            except IndexError:
                return
            if cur != "O":
                return

            b[i][j] = "#"
            flip_adjacent(b, i+1, j)
            flip_adjacent(b, i-1, j)
            flip_adjacent(b, i, j+1)
            flip_adjacent(b, i, j-1)

        height = len(board)
        for i in range(height):
            width = len(board[i])
            for j in range(width):
                # check if not edge cell
                if not (i==0 or j==0 or i==height-1 or j==width-1):
                    continue
                if board[i][j] == "O":
                    flip_adjacent(board, i, j)
        for i in range(height):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
