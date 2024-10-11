# README - Ball Sort Game

Demo Video: [https://youtu.be/OFOEqBTxC3g](https://youtu.be/OFOEqBTxC3g)

### Intro
Ball Sort Game is a simple, self-explanatory game where the user aims to sort the balls in each tube by color.

### Rules:
1. The user can only move the top ball of each tube to another tube (non-empty tube).
2. The user cannot move to and from the same tube.
3. The user can only move to tubes that are not full.
4. The game ends when all colors are sorted in each tube.

### Instructions:
1. User selects **ENTER** to move forward at each step.
2. User selects the source tube by entering an integer (0-2) indicating the tube.
3. User then selects the destination tube by entering an integer (0-2) indicating the tube.

### Features:
1. **Randomization of ball positions** - balls are shuffled and placed randomly in the tubes.
2. **Text UI** - visualization of adding and removing elements from lists shows the movement of balls among tubes (displayed in the terminal).

### Justification for Complexity:
1. **List objects** are used with elements to represent each ball in the tube.
2. The list of objects is printed **vertically** to visually represent the balls in each tube and their movement across tubes.
3. The user can only move the top ball from one tube to another (removing the lowest-index item of the source tube and updating each tube).

### Implementation (keyboard control):  
- **ENTER**: move forward and continue through each step.  
- **Enter integer 0-2**: select the source and destination tube.  
- **Levels vary** every time: lists are shuffled, and there is randomization of ball placement.

### Lists & Script Variables:
1. **Variables:**
   - `sourceTube` - input variable: indicates from which tube to move the ball.
   - `destTube` - input variable: indicates the destination tube of the ball.

2. **Lists:**
   - `new_board`: a copy of the original board used to update positions after each move.
   - `Board_lst`: 12 items in total (4 “R”s, 4 “B”s, 4 empty spaces represented as " ").
   - `Board_shuffled`: shuffles `Board_lst` and splits it into 3 sublists (4 items per list). Each sublist is rearranged so that empty spaces appear at the beginning.
     - Example:
       - `Board_lst`: ["R", "B", "R", "B", "B", "R", "B", "R", " ", " ", " ", " "]  
       - `Board_shuffled` (after sublist rearrangement):  
         - Shuffled list: ["R", " ", " ", "B", "R", "R", "B", "R", " ", "B", "B", " "]  
         - Rearranged sublists:  
           - ["R", " ", " ", "B"] → [" ", " ", "R", "B"]  
           - ["R", "R", "B", "R"] → ["R", "R", "B", "R"]  
           - [" ", "B", "B", " "] → [" ", " ", "B", "B"]

---

### Function Descriptions

#### Game Functions

- **`__main__()`**  
  - **Domain (inputs):** None  
  - **Range (outputs):** None  
  - **Behavior:** Automatically runs the game.

- **`game()`**  
  - **Domain (inputs):** None  
  - **Range (outputs):** None  
  - **Behavior:** Runs the game features, prints instructions, and asks the user for inputs (`sourceTube` and `destTube` integers).

- **`random_board()`**  
  - **Domain (inputs):** `list`  
  - **Range (outputs):** `list`  
  - **Behavior:**  
    - Takes a list and counts the number of empty spaces.  
    - Arranges the items so there are no empty spaces between them, simulating the scenario where balls are stuck at the bottom of tubes.  
    - Appends the number of empty spaces at the beginning of each tube.

- **`check_valid_move()`**  
  - **Domain (inputs):** `Board (nested list)`, `sourceTube (int)`, `destTube (int)`  
  - **Range (outputs):** `Boolean` (`TRUE=valid move`)  
  - **Behavior:** A move is valid if:  
    - The destination tube has at least one empty space.  
    - The source tube is not empty.  
    - The source tube is not the same as the destination tube.

- **`update_board()`**  
  - **Domain (inputs):** `Board (nested list)`, `sourceTube (int)`, `destTube (int)`  
  - **Range (outputs):** `Board (nested list)`  
  - **Behavior:**  
    - Updates the board if the move is valid.  
    - Checks for empty spaces in both the source and destination tubes.  
    - Identifies the last ball in the source tube and moves it to the first empty space in the destination tube.

- **`solved()`**  
  - **Domain (inputs):** `Board (nested list)`  
  - **Range (outputs):** `Boolean` (`TRUE=game solved`)  
  - **Behavior:** Checks if the game is solved, meaning all items in any tube are either "R" or "B".

---

#### Test Functions

- **`test_update_board(self)`**  
  - **Domain (inputs):** `Boards (nested lists)`, `sourceTube (int)`, `destTube (int)`  
  - **Range (outputs):** `True (updated)`  
  - **Behavior:** Verifies that the board updates correctly.

- **`test_solvedboard_solved(self)`**  
  - **Domain (inputs):** `Board (nested list)`  
  - **Range (outputs):** `True (solved)`  
  - **Behavior:** Verifies that a board where all items in any tube are the same is considered solved.

- **`test_solvedboard_notsolved(self)`**  
  - **Domain (inputs):** `Board (nested list)`  
  - **Range (outputs):** `False (not solved)`  
  - **Behavior:** Verifies that a board with mixed elements in any tube is considered not solved.

- **`test_check_valid_move_valid(self)`**  
  - **Domain (inputs):** `Board (nested list)`, `sourceTube (int)`, `destTube (int)`  
  - **Range (outputs):** `True (valid)`  
  - **Behavior:** Verifies that a move is valid when the source tube is not empty, the destination tube has at least one empty space, and the source tube is different from the destination tube.

- **`test_check_valid_move_invalid(self)`**  
  - **Domain (inputs):** `Board (nested list)`, `sourceTube (int)`, `destTube (int)`  
  - **Range (outputs):** `False (invalid)`  
  - **Behavior:** Verifies that a move is invalid when the source tube is empty, the destination tube is full, or the source tube is the same as the destination tube.

---


