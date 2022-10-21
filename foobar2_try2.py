class squarenode:
    def __init__(self,row,col,steps):
        self.row = row
        self.col = col
        self.stepstoreach = steps

def withinlimit(row,col):
    if (row >= 0 and row < 8 and col >= 0 and col < 8):
        return True
    return False
   
def solution(src, dest):
    #Your code here
    row = lambda x : int(x/8)
    col = lambda y : int(y%8)
    srcrow , srccol = row(src) , col(src)
    destrow , destcol = row(dest) , col(dest)
    rowmovements = [-2,-2,-1,-1,1,1,2,2]
    colmovements = [-1,1,-2,2,-2,2,-1,1]
    BFSqueue = []
    BFSqueue.append(squarenode(srcrow,srccol,0))
    visitednode = [[False for i in range(8)] for j in range(8)]
    visitednode[srcrow][srccol] = True

    while len(BFSqueue) > 0:
        startsquare = BFSqueue[0]
        BFSqueue.pop(0)
        if (startsquare.row == destrow and startsquare.col == destcol):
            return startsquare.stepstoreach
        
        for i in range(8):
            nextsquare_x = startsquare.row + rowmovements[i]
            nextsquare_y = startsquare.col + colmovements[i]
            if (withinlimit(nextsquare_x, nextsquare_y) and not visitednode[nextsquare_x][nextsquare_y]):
                visitednode[nextsquare_x][nextsquare_y] = True
                BFSqueue.append(squarenode(nextsquare_x, nextsquare_y, startsquare.stepstoreach + 1))

print(solution(1,2))