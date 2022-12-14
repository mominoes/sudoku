import itertools

class Cell:
    def __init__(self, val=0, row=None, col=None, box=None):
        self.candidates = set([val]) if val else set(range(1,10))
        self.row:CellContainer = row
        self.col:CellContainer = col
        self.box:CellContainer = box
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

    def naked_tuples(self, n=1):
        """If any n cells contain only the same n candidates, remove those candidates from all other cells
        Return True if any were removed, else false
        NB: n=1 is the case of a cell containing only one candidate
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

    def hidden_tuples(self, n=1):
        """If any n candidates only appear in the same n cells, remove all other candidates from those cells
        Return True if any were removed, else false
        NB: n=1 is the case of a candidate appearing only in one cell within the neighbourhood
        """
        changed = False
        candidates_appearing_upto_n_times = set()
        for can in range(1, 10):
            if len([None for cell in self.cells if can in cell.candidates]) <= n:
                candidates_appearing_upto_n_times.add(can)

        if len(candidates_appearing_upto_n_times) >= n:
            for can_tuple in itertools.combinations(candidates_appearing_upto_n_times, n):
                cells = [cell for cell in self.cells if cell.candidates.intersection(can_tuple)]
                if len(cells) == n:
                    for cell in cells:
                        if cell.candidates != cell.candidates.intersection(can_tuple):
                            cell.candidates = cell.candidates.intersection(can_tuple)
                            changed = True

        return changed