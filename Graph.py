from collections import defaultdict


class Graph:
    def __init__(self, vertices=5):
        self.vertices = vertices
        self.adjList = defaultdict(lambda:  [])

    def add_edge(self, v, w):
        self.adjList[v].append(w)

    def DFS(self, v, visited):
        """
        From one particular node
        :param v:
        :param visited:
        :return:
        """
        visited.add(v)
        print v + "-->",
        for node in self.adjList[v]:
            if node not in visited:
                self.DFS(node, visited)

    def DFS_all(self, nodes):
        visited = set()
        for node in nodes:
            if node not in visited:
                self.DFS(node, visited)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge("0", "1")
    g.add_edge("0", "2")
    g.add_edge("1", "2")
    g.add_edge("2", "0")
    g.add_edge("2", "3")
    g.add_edge("3", "3")

    print "DFS for node {}".format("2")
    g.DFS("2", set())

    print "DFS for all nodes: "
    g.DFS_all(["0", "1", "2", "3"])