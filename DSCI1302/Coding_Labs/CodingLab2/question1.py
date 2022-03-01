"""Q1. (50 points) Develop a game class that:
a) initializes by taking in integers r and c as input, this generates a
field of r rows and c columns with a bomb at a randomly chosen row and
column,
b) allows the user to play this map by asking users to find the bomb. (Name
 this method play)

**   25 points extra credit  implement the visual representation add the
necesseary logic to play minesweeper
"""

import numpy as np


class Minesweeper:

    def __init__(self, rows=10, cols=6, difficulty=1):

        self.row = None
        self.col = None
        self.rows = rows
        self.cols = cols
        self.boardArray = np.random.normal(1, 1, size=(rows, cols))
        self.boardList = [['▢'] * cols for i in range(rows)]

        self.playing = True
        self.initiate()
        self.difficulty = 1 / difficulty + 0.5

    def initiate(self):
        """Used to start the game and change settings"""

        # Defining a mean which will work as a difficulty scale from
        print("Welcome to Minesweeper! \n")
        start = input("Would you like to play?\n")

        if start.lower() == 'y':
            self.build_board()
            self.play()
        elif start.lower() == 'n':
            print("Ok ... Goodbye!")
        else:
            print("That is not a valid answer. Please enter Y or N")
            self.initiate()

    def play(self):
        # print(self.boardArray)

        while self.playing:
            # Print board
            print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.boardList]))

            # Check if won
            bombs = 0
            checked = 0
            for row in range(len(self.boardList)):
                for col in range(len(self.boardList[row])):
                    if self.boardList[row][col] == '▢' and self.boardArray[row][col] < 0:
                        bombs += 1
                    elif self.boardList[row][col] != '▢':
                        checked += 1
            if bombs + checked == len(self.boardList) * len(self.boardList[0]):
                self.you_win()

            row = int(input("Choose a row:\n")) - 1
            col = int(input("Choose a column:\n")) - 1

            if self.boardList[row][col] != '▢':
                print('This square has already been chosen. Please choose another.')
                self.play()
            elif row >= len(self.boardList) or col >= len(self.boardList):
                print("This row or column is of our board's range")
                self.play()
            else:
                self.row = row
                self.col = col

            self.check()

        print("Thanks for playing!")

    def check(self):

        if not self.boardList[self.row][self.col] == '▢' and not self.boardArray[self.row][self.col] > 0:
            self.you_win()

        if self.boardArray[self.row][self.col] < 0:
            self.you_lose()

        else:  # Continuing the game
            self.update_board()

    def build_board(self):

        changes = input("Do you want to adjust the number of rows, number of columns or difficulty? (Default: "
                        "rows = 10, columns = 6, difficulty = easy)\n")
        # Making changes
        if changes.lower() == 'y':
            # Ask for a difficulty rating between 1 and 5
            self.difficulty = input("Choose a difficulty level between 1 and 5:\n")
            # Ask fof rows and columns
            self.rows = int(input("How many rows?\n"))
            self.cols = int(input("How many columns?\n"))
        elif changes.lower() == 'n':
            self.difficulty = 1
            self.rows = 10
            self.cols = 6
        else:
            self.build_board()

        # Set up the board and playing
        mean = 1 / float(self.difficulty) + 0.5
        self.boardArray = np.random.normal(mean, 1, size=(self.rows, self.cols))
        self.boardList = [['▢'] * self.cols for i in range(self.rows)]

    def update_board(self):
        """A tool used to
         update the users board"""
        cell_num = 0
        row_range = col_range = range(3)

        # Creating new ranges to cover our edge cases
        if self.row == 0:
            row_range = range(1, 3)
        if self.col == 0:
            col_range = range(1, 3)
        if self.row == len(self.boardArray) - 1:
            row_range = range(2)
        if self.col == len(self.boardArray[0]) - 1:
            col_range = range(2)

        # Check all surrounding cells in our ranges
        for i in row_range:
            for j in col_range:
                # This covers our row and column case
                if i == 1 and j == 1:
                    pass
                # For the
                elif self.boardArray[self.row + i - 1][self.col + j - 1] < 0:
                    cell_num += 1
        self.boardList[self.row][self.col] = str(cell_num)

    def you_lose(self):

        # You hit a bomb
        print("""
                        ██████╗░░█████╗░░█████╗░███╗░░░███╗██╗
                        ██╔══██╗██╔══██╗██╔══██╗████╗░████║██║
                        ██████╦╝██║░░██║██║░░██║██╔████╔██║██║
                        ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║╚═╝
                        ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██╗
                        ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
                        \n\n                        You lose! \n\n""")

        play_again = input("Would you like to play again?\n")
        if play_again.lower() == 'y':
            # Play again
            self.build_board()
            self.play()
        else:
            self.playing = False

    def you_win(self):
        print("""
                ██╗░░░██╗░█████╗░██╗░░░██╗
                ╚██╗░██╔╝██╔══██╗██║░░░██║
                ░╚████╔╝░██║░░██║██║░░░██║
                ░░╚██╔╝░░██║░░██║██║░░░██║
                ░░░██║░░░╚█████╔╝╚██████╔╝
                ░░░╚═╝░░░░╚════╝░░╚═════╝░

                ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
                ░██║░░██╗░░██║██║████╗░██║██║
                ░╚██╗████╗██╔╝██║██╔██╗██║██║
                ░░████╔═████║░██║██║╚████║╚═╝
                ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
                ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝\n""")
        again = input("Would you like to play again?")

        if again.lower() == 'y':
            self.initiate()
        else:
            self.playing = False


x = Minesweeper()
