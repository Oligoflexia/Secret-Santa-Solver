import numpy as np
import pandas as pd

class Adjacency_Matrix:
    #row: Individual sending the gift.
    #column: Individual receiving the gift.
    
    def __init__(self, users):
        self.matrix = np.ones((len(users),
                          len(users)))
        
        for i in range(0, len(users)):
            self.matrix[i][i] = 0
        
        self.users = users
    
    #adds another participant for consideration
    def addUser(self, Person):
        self.users.append(Person)
    
    #replaces any invalid relationship in matrix with 0
    def initBans(self):
        for user in self.users:
            indexGVR = self.users.index(user)
            banlist = user.getBanlist()
            
            for bannedUser in banlist:
                indexRVR = self.users.index(bannedUser)
                
                self.matrix[indexGVR][indexRVR] = 0
    
    def getMatrix(self):
        return self.matrix
                
    def drawMatrix(self):
        df = pd.DataFrame(self.matrix)
        df.columns = self.users
        df.index = self.users
        
        print(df)
