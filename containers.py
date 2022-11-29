import itertools

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
        """If a cell contains only one candidate, remove that candidate from all other cells within container
        Return True if any was removed, else false
        """
        changed = False
        for cell in self.cells:
            if cell.got():
                for other_cell in [x for x in self.cells if x != cell]:
                    changed = changed or other_cell.remove(cell.get_single())
        return changed

    def naked_tuples(self, n=2):
        """If any n cells contain only the same n candidates, remove those candidates from all other cells
        Return True if any were removed, else false
        """
        changed = False
        for cell_tuple in itertools.combinations(self.cells, n):
            candidates = set()
            for cell in cell_tuple:
                candidates = candidates.union(cell.candidates)
                if len(candidates) > n:
                    break
            if len(candidates) > n:
                continue

            for cell_to_remove in [x for x in self.cells if x not in cell_tuple]:
                if cell_to_remove.candidates.intersection(cell.candidates):
                    cell_to_remove.candidates = cell_to_remove.candidates - cell.candidates
                    changed = True
        return changed




class Row(CellContainer):
    pass

class Col(CellContainer):
    pass

class Box(CellContainer):
    pass
