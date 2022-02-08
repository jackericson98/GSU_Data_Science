"""Q1. (50 points) Develop a game class that:
a) initializes by taking in integers r and c as input, this generates a 
field of r rows and c columns with a bomb at a randomly chosen row and 
column,
b) allows the user to play this map by asking users to find the bomb. (Name
 this method play)

**   25 points extra credit  implement the visual representation add the 
necesseary logic to play minesweeper


Q2. (50 points) Implement function wordcount() that takes a string, and 
returns the frequency of each word as a dictionary.
Note:
1. You should ignore the uppercase and lowercase. For example, 'Unicode' 
and 'unicode' are considered as the same word.
2. The punctuations and digits should NOT be counted. You only need to 
consider these punctuations: (),.!?'/[]"""
import numpy as np


class Game:

    def __init__(self, r=10, c=6):
        self.r = r
        self.c = c
        self.boardArray = np.random.normal(1, 1, size=(r, c))
        self.boardList = [['▢'] * c for i in range(r)]
        self.playing = True
        self.initiate()

    def __str__(self):
        return str(self.boardArray)

    def initiate(self):

        # Initiate the game
        global mu
        start = input("Would you like to play Minesweeper?\n")
        # Reactions to their input of our initiation question
        if start.lower() == 'y':
            changes = input("Do you want to adjust the number of rows,  number of columns or difficulty? (Default: "
                            "rows = 10, columns = 6)\n")
            if changes.lower() == 'y':
                difficulty = input("Would you like to play easy, medium or hard?\n")
                std = 1
                if difficulty.lower() == 'easy':
                    mu = 1.5
                elif difficulty.lower() == 'medium':
                    mu = 1
                elif difficulty.lower() == 'hard':
                    mu = 0.75
                self.r = int(input("How many rows?\n"))
                self.c = int(input("How many columns?\n"))
                self.boardArray = np.random.normal(mu, std, size=(self.r, self.c))
                self.boardList = [['▢'] * self.c for i in range(self.r)]
                self.play()
            else:
                self.play()
        elif start.lower() == 'n':
            print("Ok weirdo ... Goodbye!")
        else:
            print("That is not a valid answer. Please enter Y or N")
            self.initiate()

    def play(self):
        print("Welcome to Minesweeper! \n")
        print(self.boardArray)
        while self.playing:
            print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.boardList]))
            row_choice = int(input("Choose a row:\n")) - 1
            col_choice = int(input("Choose a column:\n")) - 1

            self.check(row_choice, col_choice)

    def check(self, row, col):
        if self.boardArray[row][col] < 0:
            print("""
                ██████╗░░█████╗░░█████╗░███╗░░░███╗██╗
                ██╔══██╗██╔══██╗██╔══██╗████╗░████║██║
                ██████╦╝██║░░██║██║░░██║██╔████╔██║██║
                ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║╚═╝
                ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██╗
                ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
                \n\n                        You lose! \n\n""")
            play_again = input("Would you like to play again?")
            if play_again.lower() == 'y':
                self.play()
            else:
                print("Thanks for playing!")
                self.playing = False

        else:  # Continuing the game
            surrounding_bombs = 0
            row_range = col_range = range(3)

            # Creating new ranges to cover our edge cases
            if row == 0:
                row_range = range(1, 3)
            if col == 0:
                col_range = range(1, 3)
            if row == len(self.boardArray) - 1:
                row_range = range(2)
            if col == len(self.boardArray[0]) - 1:
                col_range = range(2)

            # Check all surrounding cells in our ranges
            for i in row_range:
                for j in col_range:
                    # This covers our row and column case
                    if i == 1 and j == 1:
                        pass
                    # For the
                    elif self.boardArray[row + i - 1][col + j - 1] < 0:
                        surrounding_bombs += 1
            self.boardList[row][col] = str(surrounding_bombs)
            print("There are ", surrounding_bombs, " bombs around your cell!\n")


x = Game()
