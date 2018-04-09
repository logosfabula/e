'''
Lattice paths
Problem 15 
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
def move(position_x, position_y, moves):
    if position_x == 0 or position_y == 0:
        return 1
    else:
        if not (position_x, position_y) in moves:
            moves[(position_x, position_y)] = move(position_x - 1, position_y, moves) + move(position_x, position_y - 1, moves)
        return moves[(position_x, position_y)]
    
move(20, 20, {})