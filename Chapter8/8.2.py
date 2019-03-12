#8.2
#Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
#The robot can only move in two directions, right and down,
#but certain cells are "off limits" such that the robot cannot step on them.
#Design an algorithm to find a path for the robot from the top left to the bottom right.


def countPaths(grid,r,c,paths):
    if not validsquare(grid,r,c):
        return 0
    if isAtEnd(grid,r,c):
        return 1
    if paths[r][c] == 0 :
        paths[r][c] = countPaths(grid,r+1,c) + countPaths(grid,r,c+1)
     return paths[r][c]
