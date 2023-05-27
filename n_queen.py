class NQueenProblem:
    N = int(input("Enter the number of queens: "))

    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(board[i][j], end=" ")
            print()

    def isSafe(self, board, row, col):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper diagonal on the left side
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal on the left side
        i, j = row, col
        while j >= 0 and i < self.N:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solveNQUtil(self, board, col):
        # Base case: If all queens are placed, return True
        if col >= self.N:
            return True

        # Consider this column and try placing this queen in all rows one by one
        for i in range(self.N):
            if self.isSafe(board, i, col):
                board[i][col] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                # If placing queen in board[i][col] doesn't lead to a solution, remove the queen
                board[i][col] = 0  # BACKTRACK

        return False

    def solveNQ(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]

        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False

        self.printSolution(board)
        return True


# Driver program to test above function
if __name__ == "__main__":
    Queen = NQueenProblem()
    Queen.solveNQ()
