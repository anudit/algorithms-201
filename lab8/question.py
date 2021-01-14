from __future__ import division
import heapq, copy

class Graph(object):
    def __init__(self, numVerts, numEdges):
        self.numVerts = numVerts
        self.numEdges = numEdges
        self.edges = []                            # (v1, v2)
        self.edgeCosts = []
        self.verts = [[] for _ in range(numVerts)] # list of adj edges

    def addEdge(self, v1, v2, cost=1):
        edgeIdx = len(self.edges)
        self.edges.append((v1, v2))
        self.edgeCosts.append(cost)
        self.verts[v1].append(edgeIdx)
        self.verts[v2].append(edgeIdx)

    def getEdge(self, idx):
        return self.edges[idx]

    def getEdgeCost(self, idx):
        return self.edgeCosts[idx]

    def setEdgeCost(self, idx, cost):
        self.edgeCosts[idx] = cost
        
    def getVert(self, idx):
        return self.verts[idx]

    def getVertHead(self, idx):
        return [eIdx for eIdx in self.verts[idx]
                if self.edges[eIdx][1] == idx]

    def getVertHeadIter(self, idx):
        for eIdx in self.verts[idx]:
            if self.edges[eIdx][1] == idx:
                yield eIdx
                
    def getVertTail(self, idx):
        return [eIdx for eIdx in self.verts[idx]
                if self.edges[eIdx][0] == idx]

    def getVertTailIter(self, idx):
        for eIdx in self.verts[idx]:
            if self.edges[eIdx][0] == idx:
                yield eIdx
                
    def clone(self):
        cloned = Graph(self.numVerts, self.numEdges)
        cloned.edges = copy.deepcopy(self.edges)
        cloned.edgeCosts = copy.deepcopy(self.edgeCosts)
        cloned.verts = copy.deepcopy(self.verts)
        return cloned
    
    def __repr__(self):
        return "<Graph m=%d, n=%d, edges=%s verts=%s>" % (
            self.numEdges, self.numVerts, zip(self.edges, self.edgeCosts), self.verts)

    @staticmethod
    def loadFromFile(datafile, one_based = False):
        data = []
        f = open(datafile)
        numVerts, numEdges = [int(x) for x in f.readline().strip().split()]
        G = Graph(numVerts, numEdges)
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            parts = [int(x) for x in line.split()]
            if len(parts) == 3:
                v1, v2, cost = parts
            elif len(parts) == 2:
                v1, v2 = parts
                cost = 1
            else:
                pass
            if one_based:
                G.addEdge(v1-1, v2-1, cost)
            else:
                G.addEdge(v1, v2, cost)
        assert(G.numEdges == len(G.edges))
        f.close()
        return G

class UnionFind(object):
    def __init__(self, numItems):
        self.items = list(range(numItems))
        self.sizes = [[1] for _ in self.items]
        self.numSets = numItems

    def union(self, i, j):
        set_i = self.find(i)
        set_j = self.find(j)
        if set_i != set_j:
            self.numSets -= 1
            if self.sizes[set_i] > self.sizes[set_j]:
                self.items[set_j] = set_i
                self.sizes[set_i] += self.sizes[set_j]
            else:
                self.items[set_i] = set_j
                self.sizes[set_j] += self.sizes[set_i]

    def find(self, i):
        while self.items[i] != i:
            i = self.items[i]
        return self.items[i]

    def asDict(self):
        sets = {}
        for idx, item in enumerate(self.items):
            aSet = sets.setdefault(self.find(item), [])
            aSet.append(idx)
        return sets
        
    def __repr__(self):
        return repr(self.asDict())
		
		
from __future__ import division
import heapq

def Prim(G):
    MST = []
    T = set()
    pq = []
    T.add(1)
    for eIdx in G.getVert(1):
        heapq.heappush(pq, (G.getEdgeCost(eIdx), eIdx))
    while pq:
        cost, eIdx = heapq.heappop(pq) 
        v1, v2 = G.getEdge(eIdx)
        if v1 not in T:
            v = v1
        elif v2 not in T:
            v = v2
        else:
            continue
        T.add(v)
        MST.append(eIdx)
        for edge in G.getVert(v):
            heapq.heappush(pq, (G.getEdgeCost(edge), edge))
    return MST
        

def Kruskal(G):
    uf = UnionFind(G.numVerts)
    pq = [(G.getEdgeCost(idx), idx) for idx in range(G.numEdges)]
    heapq.heapify(pq)
    MST = []
    while uf.numSets > 1:
        eCost, eIdx = heapq.heappop(pq)
        s1, s2 = [uf.find(v) for v in G.getEdge(eIdx)]
        if s1 != s2:
            uf.union(s1, s2)
            MST.append(eIdx)
    return MST
