#!/usr/bin/python3
"""
0x05. N Queens
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    exit(1)


class nQueens:
    """This is an nQueens class."""

    def __init__(self, n):
        """The init method"""
        self.n = n
        self.col = set()
        self.posDig = set()
        self.negDig = set()
        self.results = []
        self.QueensPlacement = []
        self.board = [["."] * n for _ in range(n)]
        self.backtrack(0)

    def backtrack(self, row):
        """A method that performs the backtracking algorithm"""
        if row == self.n:
            boardList = ["".join(row) for row in self.board]
            self.results.append(boardList)
            return
        for column in range(self.n):
            a = row + column
            b = row - column
            if column in self.col or a in self.posDig or b in self.negDig:
                continue

            self.board[row][column] = "Q"
            self.col.add(column)
            self.posDig.add(row + column)
            self.negDig.add(row - column)
            self.backtrack(row + 1)
            self.col.remove(column)
            self.posDig.remove(row + column)
            self.negDig.remove(row - column)
            self.board[row][column] = "."

    def displayResult(self):
        """A method that displays the results in as indexes."""
        self.QueensPlacement = []
        for result in self.results:
            queens = []
            for rowIndex, row in enumerate(result):
                for colIndex, elem in enumerate(row):
                    if elem == "Q":
                        queens.append([rowIndex, colIndex])
            self.QueensPlacement.append(queens)
        for queens in self.QueensPlacement:
            print(queens)


chess = nQueens(n)
chess.displayResult()
