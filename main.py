import time
import random
from containers import *
from collections import defaultdict



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
        strategy_usage_stats = defaultdict(lambda: 0)
        changed = True
        while changed:
            for container in self.rows + self.cols + self.boxes:
                changed = False
                if container.candidates_once_in_container():
                    print('Candidate(s) appeared only once in container')
                    strategy_usage_stats['candidates_once_in_container'] += 1
                    changed = True
                elif container.cells_with_only_one_candidate():
                    print('Cell(s) contained only one candidate')
                    strategy_usage_stats['candidates_once_in_container'] += 1
                    changed = True
                elif container.naked_tuples(2):
                    print('Naked PAIR(s) found')
                    strategy_usage_stats['naked_pairs'] += 1
                    changed = True
                elif container.naked_tuples(3):
                    print('Naked TRIPLET(s) found')
                    strategy_usage_stats['naked_triplets'] += 1
                    changed = True
                elif container.naked_tuples(4):
                    print('Naked QUADRUPLET(s) found')
                    strategy_usage_stats['naked_quadruplets'] += 1
                    changed = True
                elif container.hidden_tuples(2):
                    print('Hidden PAIR(s) found')
                    strategy_usage_stats['hidden_pairs'] += 1
                    changed = True
                elif container.hidden_tuples(3):
                    print('Hidden TRIPLET(s) found')
                    strategy_usage_stats['hidden_triplets'] += 1
                    changed = True
                elif container.hidden_tuples(4):
                    print('Hidden QUADTRUPLET(s) found')
                    strategy_usage_stats['hidden_quadruplets'] += 1
                    changed = True

                if changed:
                    print(self)
                    time.sleep(0.01)

        print(f"\nNo more changes possible. Board solved? {self.solved()}")
        print(strategy_usage_stats)


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