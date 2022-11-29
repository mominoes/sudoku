import time
import random
from containers import *



with open('./puzzles/hard.txt', 'r') as f:
    START = random.choice(f.readlines())


class Board:
    cells: list[Cell]
    rows: list[Row]
    cols: list[Col]
    boxes: list[Box]

    def __init__(self, start="0"*81):
        # Init cells and empty rows/cols/boxes
        start = [int(x) for x in start.replace(".", "0") if x in "0123456789"]
        assert len(start) == 81
        self.cells = [Cell(val=x) for x in start]
        self.rows = [Row() for _ in range(9)]
        self.cols = [Col() for _ in range(9)]
        self.boxes = [Box() for _ in range(9)]

        for i, cell in enumerate(self.cells): # Cross-link cells and rows/cols/boxes
            row = self.rows[i // 9]
            col = self.cols[i % 9]
            box = self.boxes[3*(i//9//3) + (i%9)//3]

            row.cells.append(cell)
            col.cells.append(cell)
            box.cells.append(cell)

            cell.row = row
            cell.col = col
            cell.box = box

    def solved(self):
        for cell in self.cells:
            if not cell.got():
                return False
        return True

    def solve(self):
        changed = True
        while changed:
            changed = False
            for container in self.boxes + self.rows + self.cols:
                if container.candidates_once_in_container():
                    print('Candidate(s) appeared only once in container')
                    changed = True
                elif container.cells_with_only_one_candidate():
                    print('Cell(s) contained only one candidate')
                    changed = True
                elif container.naked_pairs():
                    print('Naked pair(s) found')
                    changed = True

                if changed:
                    print(self)
                    time.sleep(0.03)
                    break

        print(f"\nNo more changes possible. Board solved? {self.solved()}")


    def __repr__(self):
        res = ""
        for i, cell in enumerate(self.cells):
            if i%9 == 0: # Spacing bw rows
                res += "\n"
            if i%27 == 0: # Spacing bw every 3 rows
                res += "\n\n"
            if (i%9) % 3 == 0: # Spacing bw every 3 cols
                res += "   "
            res += str(cell) + "  " # Spacing bw cols
        return res + "\n" + "="*106


def main():
    board = Board(start=START)
    board.solve()


if __name__ == "__main__":
    main()