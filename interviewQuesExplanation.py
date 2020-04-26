def emptySlots(sud,l):
    for i in range(9):
        for j in range(9):
            if sud[i][j]==0:
                l[0]=i
                l[1]=j
                return True
    return False


def isPresentinRow(sud, num, row):
    for i in range(9):
        if sud[row][i]==num:
            return True
    return False


def isPresentinColumn(sud, num, col):
    for i in range(9):
        if sud[i][col]==num:
            return True
    return False


def isPresentinBox(sud, num, row, col):
    for i in range(3):
        for j in range(3):
            if sud[i+row][j+col]==num:
                return True
    return False


def valid(sud,num,row,col):
    if isPresentinRow(sud,num,row)==False and isPresentinColumn(sud,num,col)==False and isPresentinBox(sud,num,row-row%3,col-col%3)==False:
        return True
    return False

def solveSud(sud):
    l=[0,0] #container to hold emptyslot as we backtrack
    if not emptySlots(sud,l):
        return True
    row=l[0]
    col=l[1]

    for i in range(1,10):
        if valid(sud,i,row,col):
            sud[row][col]=i
            if solveSud(sud):
                return True
            sud[row][col]=0 #if your selected number didn't lead to success ,you backtrack to initial state for that position
    return False



if __name__=="__main__":
    sud=[[0 for i in range(9)] for j in range(9)]
    sud=[[0, 0, 0, 0, 0, 0, 2, 0, 0],
       [0, 8, 0, 0, 0, 7, 0, 9, 0],
       [6, 0, 2, 0, 0, 0, 5, 0, 0],
       [0, 7, 0, 0, 6, 0, 0, 0, 0],
       [0, 0, 0, 9, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 2, 0, 0, 4, 0],
       [0, 0, 5, 0, 0, 0, 6, 0, 3],
       [0, 9, 0, 4, 0, 0, 0, 7, 0],
       [0, 0, 6, 0, 0, 0, 0, 0, 0]]
    if solveSud(sud):
        for i in range(9):
            for j in range(9):
                print(sud[i][j],end=" ")
            print()
    else:
        print("Oops! Not Solvable:(")