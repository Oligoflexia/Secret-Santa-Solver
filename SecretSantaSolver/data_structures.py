import numpy as np
import pandas as pd
import random

class Person:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.banlist = []
    
    #adds a person object to the blacklist
    def banUser(self, Person):
        self.banlist.append(Person)
    
    #returns the list of banned users
    def getBanlist(self):
        return self.banlist
    
    #returns the name of the person
    def getName(self):
        return self.name
    
    #returns the email of the person
    def getEmail(self):
        return self.email

class Adjacency_Matrix:
    #row: Individual sending the gift.
    #column: Individual receiving the gift.
    
    def __init__(self, users):
        self.matrix = np.ones((len(users),len(users)))
        
        for i in range(0, len(users)):
            self.matrix[i][i] = 0
        
        self.users = users
    
    #adds another participant for consideration
    def addUser(self, Person):
        self.users.append(Person)
        
        ncolumn = np.ones(len(self.users) - 1)
        self.matrix = np.hstack(self.matrix, ncolumn)
        
        nrow = np.ones(len(self.users))
        nrow[-1] = 0
        self.matrix = np.vstack(self.matrix, nrow)
    
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
        
    def shuffleUsers(self):
        random.shuffle(self.users)
           

class Graph:
    def __init__(self, matrix):
        #adjacency matrix representation of a graph
        self.matrix = matrix.getMatrix()
        
        #Number of participants
        self.vertices = len(matrix.getMatrix())

    #cheks if the vertex being considered is a legal vertex
    def isValid(self, vertex, index, path):
        #make sure there is an edge between last vertex and considered vertex
        if self.matrix[path[index - 1] - 1] [vertex - 1] == 0:
            return False
        #make sure the vertex being considered isn't alredy in the path
        for v in path:
            if v == vertex: 
                return False
        #else return True
        return True
    
    #Recursive algorithm to find Hamiltonian Path
    def findHam(self, path, pos):
        #traversed all of the verticies
        if pos == self.vertices:
            #Does the last vertex connect to vertex 1?
            if self.matrix[path[pos - 1] - 1][path[0] - 1] == 1:
                return True
                
            else:
                return False

        #our starting point is vertex 1 so we start at vertex 2 and we want
        # to try every vertex (eventually) for a solution 
        for v in range(1 , self.vertices + 1):
            #if the vertex is valid then we add it to the path
            if self.isValid(v, pos, path) == True:
                path[pos] = v
                #we continue to recurse 
                if self.findHam(path, pos + 1) == True:
                    return True
                #if the current vertex doesn't have any possible paths
                path[pos] = 0

        return False