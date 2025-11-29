class Solution:
    def calculateMinimumHP(self, grid) -> int:

        # also look into Leetcode 2435
        
        # this is kind of a requirements problem, meaning
        # you work your way backwards
        # if the next cell takes away x amount of health
        # I should reach the cell by some_positive_value + x
        # so the dependencies here would be the cells after (r+1, c) and (r, c+1)
        
        # RECURSIVE TOP DOWN
        # m, n = len(grid), len(grid[0])
        # def recur(i, j):
        #     if i == m-1 and j == n-1:
        #         return max(-grid[i][j], 0) + 1

        #     down = right = float("inf")
        #     if i+1 < m: down = recur(i+1, j)
        #     if j+1 < n: right = recur(i, j+1)

        #     # what is the minimum requirement from this cell to the end to be alive ? 

        #     # if current cell is damaging, I need more health requirement
        #     # if current cell is health giving, I need less health requirement
        #     # if current cell gives 10, and I need 20 -> I would still require 10 =  max(-(10-20), 0)
        #     # if current cell gives 10, and I need only 5 -> I would require 0 = max(-(10-5), 0)
        #     # if current cell takes 10, and I need 20 -> I would still need 30 = max(-(-10-20), 0)
        #     # if current cell takes 10, and I need 5 -> I would still need 30 = max(-(-10-5), 0)

        #     diff = grid[i][j] - min(down, right)
        #     return max(-diff, 1)

        # return recur(0, 0)
        
        # DP TOP DOWN FORWARD
        # m, n = len(grid), len(grid[0])
        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # def recur(i, j, dp):
        #     if i == m-1 and j == n-1:
        #         return max(-grid[i][j], 0) + 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     down = right = float("inf")
        #     if i+1 < m: down = recur(i+1, j, dp)
        #     if j+1 < n: right = recur(i, j+1, dp)
        #     diff = grid[i][j] - min(down, right)
        #     dp[i][j] = max(-diff, 1)
        #     return dp[i][j]
        # return recur(0, 0, dp)

        # going from (m-1, n-1) to (0, 0) wont work in this problem because the order of operations matter. 
        # -5 -> 100 -> -50
        # while going forward tells us that only 6 initial health is required (take values from end to start)
        # if we simple reverse the direction, it would say we need 51, this is because I want to solve the problem statement which says from 0,0 to end, but trying to take values from start to end
        # I can decide with having a health of x is sufficient only if I know all the cells in the future (what damage and health)

        # survival kinds of problems (minimum health, minimum fuel, (should not drop below 0)) can only be sovled with top-down approach
        # solve subproblems (meaning look at the future states), pass that information back up. 


        # ITERATIVE SOLUTION (BOTTOM UP)
        # we need to solve it using backward loop because 
        # to solve for (r, c) -> i should have seen all future states
        # so start with the basecase (end) and move up. 

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[m-1][n-1] = max(-grid[m-1][n-1],0)+1
                    continue
                down = right = float("inf")
                if i+1 < m:
                    down = dp[i+1][j]
                if j+1 < n:
                    right = dp[i][j+1]
                diff = grid[i][j] - min(down, right)
                dp[i][j] = max(-diff, 1)
        return dp[0][0]
