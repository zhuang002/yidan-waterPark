class Node:
    id: int
    parent: Node
    children: list[Node]

    def __init__(self, id: int):
        self.parents = []
        self.id = id
        self.children = []


class Graph:
    nodes: list[Node]
    root: Node
    cache: dict

    def __init__(self):
        self.nodes = []
        self.root = None
        self.cache = {}

    def load(self):
        nNodes = int(input())
        for i in range(nNodes):
            self.nodes.append(Node(i + 1))
        self.root = self.nodes[0]

        src, tgt = map(int, input().split(' '))

        while src != 0 or tgt != 0:
            self.addPath(src, tgt)
            src, tgt = map(int, input().split(' '))

        self.cache = {}

    def addPath(self, src: int, tgt: int):
        srcNode = self.nodes[src-1]
        tgtNode = self.nodes[tgt-1]
        srcNode.children.append(tgtNode)
        tgtNode.parents.append(srcNode)

    def getPaths(self, start: int):
        if start == len(self.nodes):
            return 1

        if start in self.cache:
            return self.cache[start]

        totalPaths = 0
        for childNode in self.nodes[start-1].children:
            totalPaths += self.getPaths(childNode.id)

        self.cache[start] = totalPaths
        return totalPaths


graph = Graph()
graph.load()
paths = graph.getPaths(1)
print(paths)
