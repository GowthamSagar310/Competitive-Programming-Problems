Top-Down
1. I start at (0, 0) and ask to solve this particular case, what are the subproblems that I need to solve first ? I need to know my children's answer first.
2. I move down, and collect answers way back up. 

Bottom-Up
1. I start at a cell and ask how could I have reached this cell ? 
2. If the problem states we can only move down and right, the only way I could have reached this particular cell is from top and left. 

Especially for grid based problems (because I have the whole grid with me unlike tree / graph kind of problems)
1. Recursive Approach / Top-Down approach can be solved start from (0,0) or (end cell)
2. Iterative Approach / Bottom-Up approach can be solved by starting the loop from (0, 0) or going back in reverse (from end cell)
    1. But while solving iterative DP problems, there is no backtracking meaning there is no movement of values up / down as we do in recursive style. 
    2. So the idea here is `we have to compute the dependencies before using them`

Loop Direction for Iterative DP
1. Forward (Start -> End)
- To solve (r, c), I need to know (r-1, c) and (r, c-1)
- Since I need smaller indices to solve bigger indicies, I need to loop from (0, 0) -> (m, n)
- Example Q: What is the cheapest way to reach this cell ? 

2. Backward (End -> Start)
- Sometimes we need to look into the future to solve for the current cell. 
- Do I have enough to move forward ? These problems are requirements based. 
- If next cell needs me to have x amount of money and I spend y in current cell, I need to have x + y in the current cell, so that I still have money for the next cell.
- to solve for (r, c), I need to (r+1, c) and (r, c+1)
- Since I need bigger indices to solve for smaller, I need to loop from (m, n) to (0, 0)
- Example Q: What is minimum amount of money to start with ? 

*In most of the problems, we solve them in all 4 methods. While for some problems, one of the method will be easier to solve based on the states*