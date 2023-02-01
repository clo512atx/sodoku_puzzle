#sodoku_puzzle
import numpy as np 


puzzle= [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,0,1,9,0,0,5],
         [0,0,0,0,0,0,0,0,0]]



def accept(row, column, num):
    global puzzle
    #if number appears in the the row
    for i in range(0,9):
        if puzzle[row][i] == num:
            return False
    
    #if number appears in the column
    for i in range(0,9):
        if puzzle[i][column] == num:
            return False
    
    #if number appears in the  3x3 box, 
    '''use box_x and box_y to determine locations in grid. 
    Rows/columns(0-8)'''
    box_x= (row // 3) 
    box_y= (column // 3) 
    
    #for loop to go through every 3x3
    for i in range (box_x * 3,box_x * 3 + 3):   
        for j in range (box_y * 3, box_y* 3 + 3):
            if puzzle[i][j] == num:
                return False
    
    return True

#loop grid and fill in the empty fields

def solve():
    global puzzle
    for row in range(0,9):
        for column in range(0,9):
            if puzzle[row][column] == 0:
                for num in range (1,10):
                    if accept(row, column, num):
                        puzzle[row][column] = num
                        solve()  #recursive call
                        puzzle[row][column] = 0
                return #returns back to for loop if number is 0 until it is numbers 1-9
    
    print(np.matrix(puzzle))
    input("Other answers:")

print(solve())





    

