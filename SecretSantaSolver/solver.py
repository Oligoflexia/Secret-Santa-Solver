class Solver: 
    def __init__(self, graph):
        self.graph = graph
        
    def solve(self):
        #initialize the path list 
        path = [0] * self.graph.vertices
        #start with vertex 1
        path[0] = 1

        #no solution exists
        if self.graph.findHam(path, 1) == False:
            print("There is no Hamiltonian Cycle")
            return False

        print(path)
        return True