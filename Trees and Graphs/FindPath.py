'''
4.1 Route Between Nodes: Given a directed graph,
design an algorithm to find out whether there is a route between two nodes.
'''


# The 'defaultdict' tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container,
# but the only difference is that a 'defaultdict' will have a default value
# if that key has not been set yet.
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices #no of vertices
        self.graph = defaultdict(list) #adjacency list

    def addEdge(self, u, v):
        self.graph[u].append(v) #creating adjacency list of each vertex


    def printGraph(self):
        for vertice in self.graph:
            print "Vertex : ", vertice, " ->>> ", self.graph[vertice]

    # basic BFS
    def isThereApath(self, v1, v2):
        visited = [False]*self.vertices
        queue = []
        queue.append(v1)
        visited[v1]= True

        while queue:
            node = queue.pop()
            if node == v2:
                return "Yes, there is a path between the two"

            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u = 1
v = 3

if g.isThereApath(u, v):
    print("There is a path from %d to %d" % (u, v))
    print(g.printGraph())
else:
    print("There is no path from %d to %d" % (u, v))

u = 3
v = 1
if g.isThereApath(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))
