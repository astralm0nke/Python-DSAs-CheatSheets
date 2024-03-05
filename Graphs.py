#Units 19-21, Graphs
#DEFINITION: 
#In graphs, a "Node" is actually a "VERTEX"
#EDGE/CONNECTION exists between vertices-> no limit for ## verticies
#You can use weighed edges, such as in GOOGLE MAPS or Network Routing Protocols
#BIDIRECTIONAL graph edges gop both ways; DIRECTIONAL edges go only one way
#TREES are actually a form of graph w limit of pointing to 2 nodes, LLs are graphs that can only point to 1 node
#Know about ADJACENCY MATRICES; 1 means edge, 0 means none; or can store weights
#ADJACENCY LIST: {Vertex: [Other connected vertices]}
#SPACE COMPLEXITY: AdjMat: O(abs(V)^2), AdjList: O(abs(V)+abs(E))
#GRAPH BIG-O:
#ADD Vertex is O(1), edit is O(E), remove is O(V+E)


##CONSTRUCTOR
class Graph:
    def __init__(self):
        self.adj_list = {}
#Add Vertex fxn
    def add_V(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
#Add Edge fxn
    def add_E(self, v1, v2):
        if v1 in self.adj_list.keys and v1 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
#Remove Edge fxn
    def remove_E(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
#Remove Vertex fxn
    def remove_V(self, vertex):
#Only have to iterate thru connections assc.
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list.keys():
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

            
