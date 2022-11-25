# sudoku
Personal project for a sudoku solving engine

# Usage
No non-standard libraries needed
1. Edit the puzzle file (easy.txt, medium.txt, hard.txt)
2. `python3 main.py`

Puzzles taken from https://github.com/dimitri/sudoku

# TODOs
- Implement more strategies within one container: (1) naked/hidden pairs (2) naked/hidden triples/n-tuples,
- Implement complex strategies between 2+ containers: (1) X-Wing (2) Swordfish / n-fish
- Implement complex search-based strategies: (1) Forcing chains
- Move CellContainer and Cell classes to standalone file. Cleanup un-needed Row/Col/Box classes
- Make runnable from commandline
- Replace text representation with UI
- Include strategy / code overview in README
- Add strategy usage stats