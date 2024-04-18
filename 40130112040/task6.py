import copy 

class matrisSparse :

    def __init__(self,origin_row,origin_col, matris) -> None:
        self.sparse_matris = []
        self.origin_row = origin_row
        self.origin_col = origin_col
        self.terms = 0
        
        for i in matris:
            if(i != 0):
                self.terms += 1
        
        for i in range(origin_row):
            for j in range(origin_col):
                
                if matris[i][j] != 0:
                    row = [i,j,matris[i][j]]
                    self.sparse_matris.append(row)

    def transpose(self):

        new_matris = copy.deepcopy(self.sparse_matris)

        for i in range(len(self.sparse_matris)):
            new_matris [i][0] = self.sparse_matris [i][1]
            new_matris [i][1] = self.sparse_matris [i][0]
            

        new_matris.sort(key=lambda x: (x[0],x[1]))

        return new_matris
    

    def change(self, i,j,x):

        for k in range(self.terms):
            if self.sparse_matris[k][0] == i and self.sparse_matris[k][1] == j:
                self.sparse_matris[k][2] = x
                return
            
        
        row = [i,j,x]

        self.sparse_matris.append(row)

        self.sparse_matris.sort(key=lambda x: (x[0],x[1]))
 

    def getmat(self):
        return self.sparse_matris



a = [[0,3,0,0],[0,4,0,7],[1,0,0,0]]

s = matrisSparse(3,4,a)

print(s.getmat())
s.change(0,0,4)
print(s.getmat())
