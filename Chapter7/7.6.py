#7.6 Jigsaw Puzzle
import random

class Piece():
    def __init__(self):
        self.fits = set()
        self.connected = set()

    def fit_with(self, other):
        self.fits.add(other)
        other.fits.add(self)

    def connect(self, other):
        self.connected.add(other)
        other.connected.add(self)

class Puzzle():
    def __init__(self,n):
        self.pieces = [[]]
        pieces = [[Piece() for i in range(n)] for y in range(n)]
        for r in range(n):
            for c in range(n):
                if r:
                    pieces[r][c].fit_with(pieces[r-1][c])
                if c:
                    pieces[r][c].fit_with(pieces[r][c-1])

        self.pieces = sum(pieces, [])

        for i, _ in enumerate(self.pieces):
            j = random.randint(0, len(pieces)-1)
        self.pieces[i], self.pieces[j] = self.pieces[j], self.pieces[i]

    def is_solved(self):
        for piece in self.pieces:
            if piece.connected != piece.fits:
                return False
        return True

def solve(puzzle):
    for piece in puzzle.pieces:
        for other in puzzle.pieces:
            if other in piece.fits:
                piece.connect(other)

def main():
    puzzle = Puzzle(5)
    print(puzzle.is_solved())
    solve(puzzle)
    print(puzzle.is_solved())

if __name__ == '__main__':
    main()
