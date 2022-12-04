# sudoku
Personal project for a sudoku solving engine

# Usage
No non-standard libraries needed
1. Edit the puzzle file (easy.txt, medium.txt, hard.txt)
2. `python3 main.py`

Puzzles taken from https://github.com/dimitri/sudoku

# TODOs
- [ ] Implement more strategies within one container:
    - [x] naked pairs
    - [x] naked tuples
    - [x] hidden pairs
    - [x] hidden tuples,
- [ ] Implement complex strategies between 2+ containers:
    - [ ] X-Wing
    - [ ] Swordfish
    - [ ] n-fish
- [ ] Implement complex search-based strategies:
    - [ ] Forcing chains
- [x] Move CellContainer and Cell classes to standalone file. Cleanup un-needed Row/Col/Box classes
- [ ] Make runnable from commandline
- [ ] Replace text representation with UI
- [ ] Include strategy / code overview in README
- [x] Add strategy usage stats
- [ ] Add unit tests