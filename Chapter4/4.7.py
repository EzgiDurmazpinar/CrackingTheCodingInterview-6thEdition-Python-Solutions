def build_order(projects, dependencies):
    nodes = {} #Nodelari dictiniory'de tutuyor

    for value in projects:        #projects = a,b,c,d,e,f
        nodes[value] = GraphNode(value)  #her bir eleman icin node olusturup nodes dictiniorysine koyuyor

    for dependency in dependencies: #dependencies = (a,d),(f,b),(b,d),(f,a),(d,c)
        nodes[dependency[0]].add_edge(nodes[dependency[1]])

    queue = Queue()
    for project in projects:
        node = nodes[project]
        if not node.dependencies_left:
            queue.add(node)                  #If there is no dependency put it into queue

    build_order = []

    while queue.is_not_empty(): #queue bos degilken
        node = queue.remove()  #queue dan sil
        build_order.append(node.data) #build arrayine koy

        for dependent in node.edges:    #
            dependent.dependencies_left -= 1
            if not dependent.dependencies_left:
                queue.add(dependent)

    if len(build_order) < len(projects):
        return Exception("Cycle detected")

    return build_order

class GraphNode():
  def __init__(self, data):
    self.data = data
    self.edges = []
    self.dependencies_left = 0

  def add_edge(self, node):
    self.edges.append(node)
    node.dependencies_left += 1

class Queue():
  def __init__(self):
      self.array = []
  def add(self, item):
      self.array.append(item)
  def remove(self):
      return self.array.pop(0)
  def is_not_empty(self):
      return len(self.array) > 0

def main():
    projects = ['a','b','c','d','e','f']
    dependencies = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
    print(build_order(projects,dependencies))

if __name__ == '__main__':
    main()
