# ac3-nonogram
This program is for a research paper for CS 626: Artificial Intelligence in Ball State University's computer science program. It is designed to test the effectiveness of the AC-3 algorithm at solving [Nonograms](https://en.wikipedia.org/wiki/Nonogram). The AC-3 program was adapted into Python from a Java program used as part of the CS 626 coursework.

# Usage
The program requires nonogram clues and a solved nonogram to be provided as a .csv and .txt file respectively. These will be saved to a sub-directory in tne nonnograms directory.
The following Nonogram will be used as an example:

![image](https://github.com/user-attachments/assets/c37fd330-b4bc-4809-a5e5-64ad1a1a3921)

## Clues
* The first column of the csv represents clues for rows and the second column reperesents clues for columns.
* Clues are entered in the order they appear; top to bottom for rows, left to right for columns.
* The example Nonogram will be entered as follows:
  ```
  3,3
  1 3,1 2
  1 1,2 1
  2 2,2 2
  3,3
  ```

## Solutions
* Solutions for Nonnograms will be entered as a text filet with blank spaces entered as periods (`.`) and filled spaces entered as hashtags (`#`). Each space will be entered with a leading space.
* The example Nonogram's solution would be entered as follows:
```
 . # # # .
 # . # # #
 # . . . #
 # # . # #
 . # # # .
```
## Running
Once a nonogram's clues and solution are saved into a subdirectory, rename the `directory` variable in the main.py file to that directory. Then run the main file. The program's solution, execution time and accuracy of the program's solution will be printed.
# Limitations
The program was tested with a 5x5, 10x10, 15x15 and 25x25 nonogram. It can solve 5x5's with 100% accuracy but is less accurate with larger nonograms. 5x5 and 10x10 nonograms are solved in less than half a second, and 15x15 will take over 2 minutes.
