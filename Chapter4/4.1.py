#4.1
#Route Between Nodes: Given a directed graph and two nodes (S and E),
#design an algorithm to find out whether there is a route from S to E
from Queue import *
class Graph():
    def __init__(self):
        self.nodes = []
        self.my_queue = Queue()
    def add_node(self,node):
        self.nodes.append(node)
    def get_nodes(self):
        return self.nodes
class Node():
    def __init__(self,name):
        self.name = name
        self.adjacents = []
        self.visited = False
    def add_adjacents(self,node):
        self.adjacents.append(node)
    def get_adjacents(self):
        return self.adjacents

def breadth_first_serach(graph,start,end):
    if start == end:
        return True
    else:
        my_queue = Queue() #I have a queue to keep visited nodes
        start.visited = True
        my_queue.add(start)
        while(not my_queue.isEmpty()):
            r = my_queue.remove()
            if r != None:
                adjacents = r.get_adjacents()
                for i in range(len(adjacents)):
                    if adjacents[i].visited == False:
                        if adjacents[i] == end:
                            return True
                        else:
                            my_queue.add(adjacents[i])
                            adjacents[i].visited = True
        return False


def main():
    my_graph = Graph()
    my_node = Node('a')
    node1 = Node('b')
    node2 = Node('c')
    node3 = Node('d')
    node4 = Node('e')

    my_node.add_adjacents(node1)
    my_node.add_adjacents(node2)
    my_node.add_adjacents(node4)
    my_graph.add_node(my_node)

    print(breadth_first_serach(my_graph,my_node,node3)) #No route from my_node to node3

if __name__ == '__main__':
    main()
