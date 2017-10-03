# MazeGame

## Description:
  This is the first Machine Problem in CS440/ECE448 at UIUC. In this assignment, we build ggeneral-purpose search algorithms and apply them to solving puzzles. 
  
  There are in total 2 main parts of the project, and one extra credit part.
  
  #### Part 1: 
  We are in charge of a "Pacman" agent that needs to find paths through mazes while eating ONLY one dot, which could be thought of the classic path finding for entering and leaving the maze. We inplement four different search methods to run different maze files:
    
  - Depth-first search
    
  - Breadth-first search
    
  - Greedy best-first search

  - A* search
  
  #### Part 2: 
  We are still in charge of the "Pacman" problem, but instead of having only one dot, we have multiple dots in our maze this time. Therefore, we need to implement a revised A* algorithm with admissible heuristic function to enable the "Pacman" find relatively shorter paths to eat all the dots. The A* algorithm with admissible heuristic function should not over-estimate in any situations.
 
  #### Extra Credit: 
  We write a suboptimal search algorithm that will do a good job on a big maze. Our algorithm is the original A* algorithm.
  
## Code Files:
#### 1. DFS_PFS.py:
  This file contains the main algorithm of Depth-first search and Breadth-first search used in pt.1.
#### 2. aStar.py:
  This file contains the main algorithm of A* search.
#### 3. best_first_search.py:
  This file contians the main algorithm of Greedy best-first search.
#### 4. utility.py:
  Contains few simple data structures that are used in the algorithms, and helper function to calculate the Manhattan distance.
#### 5. readTXT.py:
  Function that reads all the *.txt* format maze file and return where is the the maze (in 2D matrix), starting point, and dots
#### 6. mainTest.py:
  Main test file for pt.1, test all algorithms running on maze files with only one dot to eat.
#### 7. a_star_multigoal.py:
  Revised A* algorithm with admissible heuristic function for running the maze in pt.2
#### 8. MST.py:
  This file contains method to construct a Minimum Spanning Tree (MST) based on the ramaining goals (all the dots left to eat).
#### 9. heuristic_multi_goal.py:
  This file sontains method to compute the admissible heuritic that we used in pt.2
#### 10. mainTestSearch.py:
  Main test file for pt.2
#### 11. extracredit.py:
  Extra credit functions
#### 12. mainTestSearch.py:
  Main test_file for extra credit
#### 13. main.py
  Top level main file that prints out all the results
 
## TXT Files:
#### For Part.1
- mediumMaze.txt
- bigMaze.txt
- openMaze.txt
#### For Part.2
- tinySearch.txt
- smallSearch.txt
- mediumSearch.txt
#### For Extra Credit
- bigDots.txt

## Contributors:
- Hua Chen
- Zekun Hu
- Caiting Wu
