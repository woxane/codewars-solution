import numpy
def sudoku(puzzle):
    global puzle
    puzle = puzzle
    solver()
    return result
    '''this module i create for run mudule below'''
result = []
def possible(y,x,n) :
    '''this module come and check can the number is possible to put in soudoku'''
    for xLIST in range(9) :
        if puzle[y][xLIST] == n :
            return False
    '''check Horizontal numbers '''
    for yLIST in range(9) :
        if puzle[yLIST][x] == n :
            return False
    '''check Vertical numbers'''
    xSQUARE = (x//3)*3
    ySQUARE = (y//3)*3
    '''ok , if we want check the sqaure and this formule can help us '''
    for row in range(3) :
        for column in range(3) :
            if puzle[ySQUARE+row][xSQUARE+column] == n :
                return False
    return True
def solver():
    global puzle
    global result
    for y in range(9) :
        for x in range(9):
            if puzle[y][x] == 0 :
                '''if we want solve the sudoku we must find empty(0 in here) grid'''
                for n in range(1,10) :
                    if possible(y,x,n) :
                        '''and if the module possible pass true to us we put the correct number in grid'''
                        puzle[y][x] = n
                        solver()
                        puzle[y][x] = 0
                return
    result = numpy.array(puzle).tolist() 
