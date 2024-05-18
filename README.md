# Sudoku-Solver-with-GUI

## Contents

1. [Summary](#summary)
1. [Program Structure](#program-structure)
   - [Modules](#modules)
1. [Code and Approach](#code-and-approach)
   - [Solving the puzzle - Backtracking](#solving-the-puzzle---backtracking)
   - [GUI](#gui)

## Summary

This program was built to solve sudoku problems. Allows the user to input the sudoku puzzle in a generated grid which can be solved in <1 second. The output includes the solved puzzle (indicating which values are solved values and ones that are given) as well as the time taken for the computer to solve and the number of calculations that were required.

## Installation

TODO // install instructions and running .exe file

## Program Structure

- [_solveSudoku.py_](solveSudoku.py) : contains subroutines for the logic of solving a sudoku puzzle.
- [_sudokuGUI.py_](sudokuGUI.py) : contains the app and classes

### Modules

- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) : used to create GUI and placing classes into frames.
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) : import only the Canvas class as not available in customtkinter - used for creating filled shapes that were used as grid lines within the `SudokuGrid()` and `AnswerGrid()` classes.
- [`time`](https://docs.python.org/3/library/time.html) : used to track how long the backtracking algorithim took to solve the puzzle.
- [`copy`](https://docs.python.org/3/library/copy.html) : used to duplicate the puzzle so that `zeroPuzzle` could be initialised to keep track of original puzzle before placed solve values

## Code and Approach

### Solving the puzzle - Backtracking

This app takes the common brute force approach to solving a sudoku puzzle by trying possible cases and backtracking when an attempt is invalid.

### GUI

The overall structure of the app follows the object-oriented structure recommended in the customtkinter documentation. <br>

- `MainFrame(ctk.CTkFrame)` class contains all frames of the program
- `SudokuGrid(ctk.CTkFrame)` class contains the input grid for sudoku puzzle
- `AnswerGrid(ctk.CTkFrame)` class contains the labels which get updated to the solved sudoku

## Potential Improvements

- Backtracking Algorithm - considering heuristics for faster completion

## Preview

![Screenshot of sudoku solver puzzle solved](https://github.com/09jayy/09jayy/blob/main/assets/Sudoku-Solver-with-GUI/solved-puzzle-screenshot.png?raw=true)
