import random
import copy



def update_board(board, sourceTube, destTube):
    """
    This function updates the entire board if move is valid.

    Parameters
    -----
    board: nested list
    sourceTube: int
    destTube: int

    Returns
    -------
    new_board: nested list
    """
    new_board = copy.deepcopy(board)
    if check_valid_move(board, sourceTube, destTube) == False:
        print("Invalid Move. Try again :(")
        return board
    else:
        for dest_i in range(4):  # check empty space for destination tube
            if new_board[int(destTube)][dest_i] == " ":
                continue
            else:
                dest_i -= 1
                break

        for source_i in range(4): # check empty space for source tube
            if new_board[int(sourceTube)][source_i] == " ":
                continue
            else:
                break

        new_board[int(destTube)][dest_i] = new_board[int(sourceTube)][source_i]
        new_board[int(sourceTube)][source_i] = " "

        print("Updated Board:")
        print("   tube0        tube1        tube2")
        print(" \       /    \       /    \       /")
        print(f" |   {new_board[0][0]}   |    |   {new_board[1][0]}   |    |   {new_board[2][0]}   |")
        print("  -------      -------      -------")
        print(f" |   {new_board[0][1]}   |    |   {new_board[1][1]}   |    |   {new_board[2][1]}   |")
        print("  -------      -------      -------")
        print(f" |   {new_board[0][2]}   |    |   {new_board[1][2]}   |    |   {new_board[2][2]}   |")
        print("  -------      -------      -------")
        print(f" |   {new_board[0][3]}   |    |   {new_board[1][3]}   |    |   {new_board[2][3]}   |")
        print("  -------      -------      -------")

        return new_board


def game():
    """
    This function runs the game.
    """

    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    print("     ")
    print("(づ˶•༝•˶)づ ᳂᳂᳂᳂  Welcome to Ball Sort Game!! ๋࣭ ⭑")
    print("     ")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    print("     ")
    input("Press Enter to continue...")
    print("     ")
    print("For each game, there will be three tubes.")
    print("There will be 4 RED balls and 4 BLUE balls in total. Red balls are denoted as 'R', and blue balls are denoted as 'B'.")
    input("In each game, the order of balls will be randomized. Press Enter to continue...")
    print("     ")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    print("     ")
    print("Your mission is to sort the balls such that each tube will only have balls with the same color.")
    input("Are you READY?? Press Enter to continue...")
    
    
    board_lst = ["R", "B", "R", "B", "B", "R", "B", "R", " ", " ", " ", " "] # List of all "R"s, "B"s, and empty strings (4 each)
    random.shuffle(board_lst) # Shuffle all elements in the list 
    
    
    def random_board(lst):
        """
        This fucntion checks if the move is valid.

        Parameters
        -----
            lst: original list

        Returns
        -------
            lst: list with spaces reordered

        """
        result = []
        num_space = 0
        for i in range(len(lst)):
            if lst[i] == " ":
                num_space += 1  # count the number of spaces in list
            else:
                result.append(lst[i]) # put the items that are not empty together
        for i in range(num_space):
            result.append(" ") # put back the spaces back to the top of respective list
        return result
    
    # Shuffled and rearranged board
    board_shuffled = [
        list(reversed(random_board(board_lst[0:4]))), 
        list(reversed(random_board(board_lst[4:8]))), 
        list(reversed(random_board(board_lst[8:13])))
    ]

    print("The starting tubes are: ")
    print("   tube0        tube1        tube2")
    print(" \       /    \       /    \       /")
    print(f" |   {board_shuffled[0][0]}   |    |   {board_shuffled[1][0]}   |    |   {board_shuffled[2][0]}   |")
    print("  -------      -------      -------")
    print(f" |   {board_shuffled[0][1]}   |    |   {board_shuffled[1][1]}   |    |   {board_shuffled[2][1]}   |")
    print("  -------      -------      -------")
    print(f" |   {board_shuffled[0][2]}   |    |   {board_shuffled[1][2]}   |    |   {board_shuffled[2][2]}   |")
    print("  -------      -------      -------")
    print(f" |   {board_shuffled[0][3]}   |    |   {board_shuffled[1][3]}   |    |   {board_shuffled[2][3]}   |")
    print("  -------      -------      -------")

    while True:
        sourceTube = input("Choose the tube you want the ball to move from (ENTER an integer from 0-2)...")
        while (sourceTube not in ["0", "1", "2"]):
            sourceTube = input("Choose the tube you want the ball to move from (ENTER an integer from 0-2)...")
        
        destTube = input("Choose the destination tube you want the ball to move to (ENTER an integer from 0-2)...")
        while (destTube not in ["0", "1", "2"]):
            destTube = input("Choose the tube you want the ball to move from (ENTER an integer from 0-2)...")
        
        board_shuffled = update_board(board_shuffled, sourceTube, destTube)
        if solved(board_shuffled):
            print("BALLS ARE ALL SORTED! CONGRATS :> (omedetou~) -.- -.- -.-")
            break

def check_valid_move(board, sourceTube, destTube):
    """
    This fucntion checks if the move is valid.

    Parameters
    -----
        board
        sourceTube
        destTube

    Conditions
    -------
        Cannot move from and to the same list
        Cannot move from an empty list
        Cannot move to a full list

    Returns
    -------
        type: boolean
        brief: True if move is valid, False otherwise.

    """
    if int(destTube) == int(sourceTube):
        return False
    
    if board[int(destTube)][0] == " ":
        if board[int(sourceTube)][3] != " ":
            return True
    else:
        return False
    
        
def solved(board):
    for tube in range(3):
        if all(x == "B" for x in board[tube]):
            for tube in range(3):
                if all(x == "R" for x in board[tube]):
                    return True
    return False

def __main__():
    game()

__main__()

# -----------
# Test cases

import unittest
import game
from game import update_board, solved, check_valid_move

class Testgame(unittest.TestCase):
    
    def test_update_board(self):
        board1 = [[" ","B","B","B"], ["R","R","R","R"], [" "," "," ","B"]]
        board2 = [["B","B","B","B"], ["R","R","R","R"], [" "," "," "," "]]
        result = game.update_board(board1, 2, 0)
        self.assertTrue(result == board2)
        #   Checks to see if board1 will update into board2, should return True


    def test_solvedboard_solved(self):
        board = [["B","B","B","B"], ["R","R","R","R"], [" "," "," "," "]]
        self.assertTrue(game.solved(board))
        #   All balls are sorted (all items in any tube is the same element) is considered solved board, so it should return True 
    
    def test_solvedboard_notsolved(self):
        board = [[" "," ","B","R"], [" ","R","B","B"], [" ","B","R","R"]]
        self.assertFalse(game.solved(board)) 
        #   Any tube has mixed elements is considered not solved, thus it should return False      


    def test_check_valid_move_valid(self):
        board = [["B","R","B","R"], [" ","R","B","B"], [" "," "," ","R"]]
        self.assertTrue(game.check_valid_move(board,1,2))
        self.assertTrue(game.check_valid_move(board,2,1))
        self.assertTrue(game.check_valid_move(board,0,1))
        #   A move is considered valid if the source tube is not empty, and the destination tube has at least one empty space, and source tube is different from destination tube.

    def test_check_valid_move_invalid(self):
        board = [["R","R","B","B"], ["R","B","B","R"], [" "," "," "," "]]
        self.assertFalse(game.check_valid_move(board,2,1))
        self.assertFalse(game.check_valid_move(board,0,1))
        self.assertFalse(game.check_valid_move(board,0,0))
        #   A move is considered invalid if the source tube is empty, or the destination tube is full, or source tube is the same as destination tube.



if __name__ == '__main__':
    unittest.main()