import customtkinter as ctk
import solveSudoku 
from tkinter import Canvas
import time
import copy

# CONSTANTS
FONT = ("Helvetica",14)
FONT_BOLD = ("Calibri bold",16)
# SCALING
WINDOW_DIM = "1510x880"


# SUBROUTINES
def placeCol(master,col,row):
    canvas = Canvas(master,width=5,height=75,bg="black", highlightthickness=0)
    canvas.grid(column=col,row=row)

def placeRow(master,row,col):
    canvas = Canvas(master,width=75,height=5,bg="black", highlightthickness=0)
    canvas.grid(column=col,row=row)

def fillGap(master,row,col):
    canvas = Canvas(master,width=5,height=5,bg="black", highlightthickness=0)
    canvas.grid(column=col,row=row)

# CLASSES
class AnswerGrid(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid(column=3,row=1,sticky="e")
        aRow = 0
        aCol = 0
        self.boxes = []

        for rowNum in range(11):
            if (rowNum == 3 or rowNum == 7):
                for i in range(11):
                    if i != 3 and i != 7:
                        placeRow(self,rowNum,i)
                    else:
                        fillGap(self,rowNum,i)
            else:
                aCol = 0
                boxRow = []
                for columnNum in range(11):
                    if columnNum == 3 or columnNum == 7:
                        placeCol(self,columnNum,rowNum)
                    else:
                        box = ctk.CTkLabel(master=self,text="",width=75,height=75)
                        box.grid(row=rowNum,column=columnNum,sticky="e")
                        boxRow.append(box)
                        aCol += 1
                aRow += 1
                self.boxes.append(boxRow)
    
    def newSolve(self,puzzle: list[list[int]],zeroPuzzle:list[list[int]] = []):
        for aRow,boxRow in enumerate(self.boxes):
            for aCol,box in enumerate(boxRow):
                box.configure(text=puzzle[aRow][aCol],text_color="grey" if zeroPuzzle[aRow][aCol] != 0 else "white",font=FONT) if puzzle != [] else box.configure(text="")


class SudokuGrid(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid(column=1,row=1)
        self.dimen = 75
        self.entries = []

        for rowNum in range(11):
            if (rowNum == 3 or rowNum == 7):
                for i in range(11):
                    if i != 3 and i != 7:
                        placeRow(self,rowNum,i)
                    else:
                        fillGap(self,rowNum,i)
            else:
                rowEntries = []
                for colNum in range(11):
                    if colNum == 3 or colNum == 7:
                        placeCol(self,colNum,rowNum)
                    else:
                        entry = ctk.CTkEntry(self, placeholder_text="", width=self.dimen, height=self.dimen, corner_radius=0)
                        entry.grid(column=colNum, row=rowNum)
                        rowEntries.append(entry)
            
                self.entries.append(rowEntries)

    def solvePuzzle(self,answerGrid: list[list[int]],status: ctk.CTkLabel,calculations: ctk.CTkLabel):
        puzzle: list[list[int]] = []

        for entry_row in self.entries:
            row = []
            for entry in entry_row:
                if entry.get() != "" and entry.get() != 0:
                    row.append(int(entry.get()))
                else:
                    row.append(0)
            puzzle.append(row)

        zeroPuzzle = copy.deepcopy(puzzle)

        if solveSudoku.checkInputValid(puzzle) == True:
            # SOLVE PUZZLE
            startTime: time = time.time()
            puzzle,calNum = solveSudoku.solveSudoku(puzzle)
            endTime: time = time.time()

            # UPDATE STATUS MESSAGES
            status.configure(text=f"Solved in {round(endTime-startTime,6)} seconds")  
            calculations.configure(text=f"Calculations: {calNum:,}")
            
            # UPDATE ANSWER GRID
            answerGrid.newSolve(puzzle,zeroPuzzle)
        else:
            puzzle = []
            status.configure(text="Invalid Input - Unsolvable Puzzle")
            calculations.configure(text="")
            answerGrid.newSolve(puzzle)
    
    def clearPuzzle(self):
        for entry_row in self.entries:
            for entry in entry_row:
                entry.delete(0,"end")

class Blank(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=20,fg_color="transparent")
        self.grid(column=2,row=1)
        
# MAIN FRAME CLASS
class MainFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(padx=60,pady=30, fill="both",expand = True)

        # FRAMES
        self.sudokuGrid = SudokuGrid(self)
        self.blank = Blank(self)
        self.answerGrid = AnswerGrid(self)

        # LABELS AND BUTTONS
        # Empty label
        self.empty1 = ctk.CTkLabel(self, text="")
        self.empty1.grid(column=1,row=11)
        self.empty2 = ctk.CTkLabel(self, text="")
        self.empty2.grid(column=1,row=13)

        # Status labels
        self.status = ctk.CTkLabel(master=self,text="",width=50,font=FONT_BOLD)
        self.status.grid(column=3,row=12)
        
        self.calculations = ctk.CTkLabel(master=self,text="",width=50,font=FONT)
        self.calculations.grid(column=3,row=13)

        # Solve Button
        self.submit = ctk.CTkButton(master=self, text="Solve", width = 150, font=FONT_BOLD,command=lambda: self.sudokuGrid.solvePuzzle(self.answerGrid,self.status,self.calculations))
        self.submit.grid(column=1, row=12)

        # Clear button
        self.clear = ctk.CTkButton(master=self, text="Clear", width = 150, font=FONT,command=lambda: self.sudokuGrid.clearPuzzle())
        self.clear.grid(column=1, row=14)

# MAIN APP CLASS
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(WINDOW_DIM)
        self.title("SUDOKU SOLVER - BY JAYツ")
        self.frame = MainFrame(self)

# MAIN
def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    ctk.deactivate_automatic_dpi_awareness()
    app = App()
    app.iconbitmap("sudokuIcon.ico")
    app.mainloop()

if __name__ == "__main__":
    main()