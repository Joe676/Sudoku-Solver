import random

class board:
    bo = []
    temp = []
    size = 9
    def __init__(self, seed = 0):
        for i in range(self.size):
            self.bo.append([])
            for j in range(self.size):
                self.bo[i].append(0)
        if(seed != 0):
            random.seed(seed)

    #def removeRandom(self, left):

    def Solve(self, x = 0, y = 0, Gen = False):
        #check next free space
        #create posibilities vector
        #try each:
            #if isnt wrong write in and (return)recurse to next position
            #if is wrong try next
            #if no next return false
        #FOR GENERATING RANDOMIZE POSIBILITIES

        if(x>=self.size):
            x = 0
            y += 1
        if(y>=self.size):
            return True
        if self.bo[x][y] != 0:
            return self.Solve(x+1, y)
        
        pos = [i for i in range(1, 10)]
        if(Gen == True):
            random.shuffle(pos)
        solved = False

        while(len(pos)>0):
            self.bo[x][y] = pos.pop()
            #print("DEBUG LOG: tried: {}".format(self.bo[x][y]))
            if(self.valid(x, y)):
                solved = self.Solve(x+1, y)
            if solved == True:
                return True
        self.bo[x][y] = 0
        return False

    def Generate(self, x = 0, y = 0):
        #create random posibilities vector
        #try each:
            #if isnt wrong write in and (return)recurse to next position
            #if is wrong try next
            #if no next return false
        #return self.Solve(x, y, True)
        if(x>=self.size):
            x = 0
            y += 1
        if(y>=self.size):
            return True
        
        pos = [i for i in range(1, 10)]
        random.shuffle(pos)
        solved = False

        while(len(pos)>0):
            self.bo[x][y] = pos.pop()
            #print("DEBUG LOG: tried: {}".format(self.bo[x][y]))
            if(self.valid(x, y)):
                solved = self.Generate(x+1, y)
            if solved == True:
                return True
        return False
        
    def valid(self, x, y):
        for i in range(x-1, -1, -1):
            if self.bo[x][y] == self.bo[i][y]:
                return False
        for j in range(y-1, -1, -1):
            if self.bo[x][y] == self.bo[x][j]:
                return False
        if not self.checkSquare(x, y):
            return False
        return True
    
    def checkSquare(self, x, y):
        squareIndexX = x//3
        squareIndexY = y//3
        for i in range(squareIndexX * 3, squareIndexX * 3 + 3):
            for j in range(squareIndexY * 3, squareIndexY * 3 + 3):
                if (i != x or j != y) and self.bo[x][y] == self.bo[i][j]:
                    return False
        return True
        

    def Show(self):
        for row in self.bo:
            print(row)
    #def Solve(self):

if __name__ == "__main__":
    Sudoku = board()
    #print(Sudoku.Generate())
    #Sudoku.Show()
    ref = [[], [], [], [], [], [], [], [], []]
    ref[0] = [2, 5, 8, 9, 6, 1, 0, 4, 7]
    ref[1] = [1, 0, 9, 2, 0, 3, 0, 0, 8]
    ref[2] = [0, 6, 0, 8, 7, 0, 2, 0, 0]
    ref[3] = [0, 3, 0, 0, 8, 9, 1, 0, 4]
    ref[4] = [0, 0, 0, 1, 2, 7, 5, 8, 3]
    ref[5] = [0, 2, 1, 0, 3, 4, 0, 0, 0]
    ref[6] = [0, 1, 0, 3, 9, 8, 4, 6, 2]
    ref[7] = [0, 8, 0, 0, 0, 2, 9, 3, 5]
    ref[8] = [0, 0, 0, 0, 5, 6, 0, 0, 0]
    Sudoku.bo = ref.copy()
    Sudoku.Show()
    s = Sudoku.Solve()
    print(s)
    if(s):
        Sudoku.Show()