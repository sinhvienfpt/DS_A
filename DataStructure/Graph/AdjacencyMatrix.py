# Adjacency Matrix representation of a graph
class Graph:
    # self represents the instance of the class. 
    # By using the “self” keyword we can access the 
    # attributes and methods of the class in python.
    # It binds the attributes with the given arguments.

    # This constructor is used to initialize the adjacecny matrix
    # with 0.
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
    

    # This function prints the adjacency matrix of the graph
    # Due to two nested loops, it is O(V^2)
    def printGraph(self):
        print("\nAdjacency Matrix:")
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end = " ")
            print()
    
    # This function is used to add an edge
    # between vertices v and w.
    # This implementation is for undirected graph
    def addEdge(self, v, w):
        print("Adding an edge between", v , "and", w , "and between", w , "and", v)
        self.graph[v][w] = 1
        self.graph[w][v] = 1
    

    # This function is used to add a
    # vertex to the graph.
    def addVertex(self, v):
        self.V += 1
        for i in range(self.V-1):
            self.graph[i].append(0)
        self.graph.append([0 for column in range(self.V)])
    

if __name__ == "__main__":

    # Initialize the graph with 5 vertices
    g = Graph(5)

    # An edge between 0 and 1 and between 1 and 0 will be created
    g.addEdge(0, 1)

    # An edge between 0 and 2 and between 2 and 0 will be created
    g.addEdge(0, 2)

    # An edge between 1 and 2 and between 2 and 1 will be created
    g.addEdge(1, 2)

    # An edge between 2 and 0 and between 2 and 0 will be created
    g.addEdge(2, 0)

    # An edge between 2 and 3 and between 3 and 2 will be created
    g.addEdge(2, 3)

    # An edge between 3 and 4 and between 4 and 3 will be created
    g.addEdge(3, 4)
    g.printGraph()