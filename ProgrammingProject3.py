from ProgrammingProject3Timer import time_method
import math

# Provided by Dr. Emily Kaplitz

class Graph:
    
    """Creates an empty adjacency list called aList. This function uses a dictionary. You will be able to access the
        list per vertex by using v.
        V - A list of Vertices
        E - A list of Edges. This list needs to be a list of tuples.
        directed - Controls whehther the graph is a digraph or not"""
    def __init__(self, V, E, directed):
        self.aList = []
        
        for v in range(len(V)):
            self.aList.append([])
            
        for e in E:
            self.addEdge(e[0], e[1], directed)

    """Creates an edge. If directed is true, only one direction will be added. If not, both directions will be added
        v1 - The first vertex that makes up the edge
        v2 - The second vertex that makes up the edge
        directed - Controls whehther the graph is a digraph or not"""
    def addEdge(self, v1, v2, directed):
        if not directed: 
            self.aList[v1].append(v2)
            self.aList[v2].append(v1)
        else:
            self.aList[v1].append(v2)

    """Prints the Adjacency List."""
    def printGraph(self):
        count = 0
        for v in self.aList:
            print(count, ": ", v)
            count =  count + 1

            
    """Returns the degree of specified vertex.
        v - The vertex you want to get the degree of
        Return:
            len(self.aList[v]) - The number of edges coming out of the vertex."""
    def degree(self, v):
        return len(self.aList[v])

    """Returns the degree of specified vertex.
        v - The vertex you want to get the degree of
        Return:
            len(self.aList[v]) - The number of edges coming out of the vertex."""
    def degree(self, v):
        return len(self.aList[v])




    ''' 2 Seperate DFS methods, 1 for regular and SCC & the other for Topological Sort
    '''    

    def DFS(self, s):
        ##Implement DFS from the psuedocode given in the slides (s is the source you want to start with. You will need this for SCC)
        NumberOfVertices = len(self.aList)

        self.color = ["white"] * NumberOfVertices
        self.pi = [None]  * NumberOfVertices
        self.time = 0
        self.d = [0] * NumberOfVertices
        self.f = [0] * NumberOfVertices

        if self.color[s] == "white":
            self.DFSVisit(s)

        for u in range(NumberOfVertices):
            if self.color[u] == "white":
                self.DFSVisit(u)


    def DFSforTopoSort(self):       # couln't find a way to use DFS(self, s) without adding a starting node parameter
        NumberOfVertices = len(self.aList)         # to the TopologicalSort method making it TopologicalSort(self, s)
        self.color = ['white'] * NumberOfVertices
        self.pi = [None] * NumberOfVertices
        self.d = [0] * NumberOfVertices
        self.f = [0] * NumberOfVertices
        self.time   = 0

        for u in range(NumberOfVertices):
            if self.color[u] == 'white':
                self.DFSVisit(u)


    '''Needing 2 seperate visiting methods 
    '''

    def DFSVisit(self, u):
        ##Implement DFS Visit from the psuedocode given in the slides

        self.time += 1
        self.d[u] = self.time
        self.color[u] = "gray"

        for v in self.aList[u]:
            if self.color[v] == "white":
                self.pi[v] = u
                self.DFSVisit(v)

        self.color[u] = "black"
        self.time += 1
        self.f[u] = self.time


    def DFSVisitForSCC(self, u):
        self.color[u] = 'gray'
        self.current_component.append(u)

        for v in self.aList[u]:
            if self.color[v] == 'white':
                self.DFSVisitForSCC(v)

        self.color[u] = 'black'


    def DFS_SCC(self, s):
        if self.color[s] == "white":
            self.DFSVisitForSCC(s)

    
    
    def TopologicalSort(self):
        ##Implement Topological Sort from the psuedocode given in the slides
        LinkedList = []

        self.DFSforTopoSort()

        vertices = list(range(len(self.f)))
        vertices.sort(key=lambda v: self.f[v], reverse=True)

        for v in vertices:
            LinkedList.append(v)

        return LinkedList





    def Transpose(self):
        ##Implement a Graph Transopose to be used in the Strongly Connected Components function
        NumberOfVertices = len(self.aList)
        GT = Graph(list(range(NumberOfVertices)), [], directed=True)         

        for u in range(NumberOfVertices):
            GT.aList[u] = []

        for u in range(NumberOfVertices):
            for v in self.aList[u]:
                GT.aList[v].append(u)

        return GT


    def SCC(self):
        ##Implement Strongly Connected Components from the psuedocode given in the slides
        
        self.DFSforTopoSort()

        GT = self.Transpose()

        order = []
        for v in range(len(self.f)):
            order.append((self.f[v], v))
        order.sort(reverse=True)

        NumberOfVertices = len(GT.aList)
        GT.color = ['white'] * NumberOfVertices
        GT.pi = [None] * NumberOfVertices
        GT.d =  [0] * NumberOfVertices
        GT.f = [0] * NumberOfVertices
        GT.time    = 0   

        for (finish, u) in order:
            if GT.color[u] == 'white':
                GT.current_component = []
                GT.DFS_SCC(u)
                print(GT.current_component)



if __name__ == "__main__":

    V = [0, 1, 2, 3, 4, 5]
    E = [(0, 1), (0, 2), (1, 3), (4, 3), (4, 5), (5, 4)]

    G = Graph(V, E, directed=True)

    print("Adjacency List:")
    G.printGraph()


    startingVertex = 0
    print('\n' + "DFS")
    G.DFS(startingVertex)

    print('\n' + "Topolocical Sort")
    decreasingOrder = G.TopologicalSort()
    print(decreasingOrder)

    print("SCC")
    G.SCC()


    print(V)
    print("Discovery times:", G.d)
    print("Finish times:   ", G.f)
    print("Parents:         ", G.pi)



    print()
    print()

    time_method(G.DFSforTopoSort)
    time_method(G.TopologicalSort)
    time_method(G.SCC)
