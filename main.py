from dataclasses import dataclass
import random
import time
import uuid

class Cell:
    def __init__(self, val=0, row=None, col=None, box=None):
        self.candidates = set([val]) if val else set(range(1,10))
        self.row:Row = row
        self.col:Col = col
        self.box:Box = box
        self.got = lambda : len(self.candidates) == 1
        self.get_single = lambda : next(iter(self.candidates)) if self.got() else None

    def set(self, val):
        if len(self.candidates) != 1 or val not in self.candidates:
            self.candidates = set([val])
            return True
        return False

    def remove(self, val):
        if val in self.candidates:
            self.candidates.remove(val)
            return True
        return False

    def __str__(self):
        delimiter = "`" if self.got() else "_"
        res = ""
        for i in range(1, 10):
            if i in self.candidates:
                res += str(i)
            else:
                res += delimiter
        return res


# @dataclass
class CellContainer():
    cells: list[Cell]
    def __init__(self):
        self.cells = []

    def __str__(self):
        return str([str(cell) for cell in self.cells])

    def candidates_once_in_container(self):
        """For candidates appearing only in one cell within a container, remove all other candidates from that cell.
        Return True if any were removed, else false
        """
        changed = False
        for can in range(1, 10):
            appearances = 0
            for cell in self.cells:
                if can in cell.candidates:
                    last_cell = cell
                    appearances += 1
                if appearances > 1:
                    break
            if appearances == 1:
                changed = changed or last_cell.set(can)

        return changed


    def cells_with_only_one_candidate(self):
        """If a cell contains only one candidate, remove that candidate from all other cells within container"""
        changed = False
        for cell in self.cells:
            if cell.got():
                for other_cell in self.cells:
                    if cell != other_cell:
                        changed = changed or other_cell.remove(cell.get_single())
        return changed



class Row(CellContainer):
    pass

class Col(CellContainer):
    pass

class Box(CellContainer):
    pass

START = """
85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.
"""

# @dataclass
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


        for lis in [self.rows, self.cols, self.boxes]: # Print rows/cols/boxes
            for item in lis:
                print(item)
            print()

    def solve(self):
        changed = True
        while changed:
            changed = False
            for container_list in [self.boxes + self.rows, self.cols]:
                for container in container_list:
                    if container.candidates_once_in_container() or container.cells_with_only_one_candidate():
                        print(self)
                        time.sleep(0.05)
                        changed = True

    def __repr__(self):
        res = "\n" + "="*105
        for i, cell in enumerate(self.cells):
            if i%9 == 0: # Spacing bw rows
                res += "\n"
            if i%27 == 0: # Spacing bw every 3 rows
                res += "\n\n"
            if (i%9) % 3 == 0: # Spacing bw every 3 cols
                res += "   "
            res += str(cell) + "  " # Spacing bw cols
        return res



def main():
    board = Board(start=START)
    board.solve()


if __name__ == "__main__":
    main()