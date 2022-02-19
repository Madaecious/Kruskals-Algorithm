####################################################################################
# Finds the Minimum Spanning Tree of a Graph Using Kruskal's Algorithm.
# Uses the Greedy Approach and the Disjoint Method.
# -----------------------------------------------------------------------
# Mark Barros - BID 013884117
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
####################################################################################

# This is an import needed for reading csv files.
import csv

# This is a class for representing disjoint sets.
class DisjointSet:
    parent = {}
 
    # This performs the Makeset operation.
    def makeSet(self, N):
 
        # This creates N disjoint sets (one for each vertex).
        for i in range(N):
            self.parent[i] = i
 
    # This finds the root of the set in which element k belongs.
    def Find(self, k):
 
        # This handles case k equals the root (base case).
        if self.parent[k] == k:
            return k
 
        # This searches for the parent until the root is found (recursive case).
        return self.Find(self.parent[k])
 
    # This performs a union of two subsets.
    def Union(self, a, b):
 
        # This finds the root of the sets in which elements x and y belong.
        x = self.Find(a)
        y = self.Find(b)
        self.parent[x] = y
 
 
# This constructs the MST using Kruskal’s algorithm.
def kruskalAlgorithm(edges, N):
 
    # This stores the edges present in the MST.
    MST = []
 
    # This initializes the DisjointSet class and creates a singleton set for
    # each element of the universe.
    disjoint_set = DisjointSet()
    disjoint_set.makeSet(N)
 
    index = 0
 
    # Sort edges by increasing weight
    edges.sort(key=lambda x: x[2])
 
    # The MST contains exactly V-1 edges
    while len(MST) != N - 1:
 
        # This considers the next edge with minimum weight from the graph.
        (source, destination, weight) = edges[index]
        index = index + 1
 
        # This finds the root of the sets to which two endpoint
        # vertices of the next edge belongs.
        x = disjoint_set.Find(source)
        y = disjoint_set.Find(destination)
 
        # This determines if both endpoints have different parents. If so, they
        # belong to different connected components and can be included in MST.
        if x != y:
            MST.append((source, destination, weight))
            disjoint_set.Union(x, y)
 
    return MST
 
 # Program execution starts here.
if __name__ == '__main__':

    # This will initially hold the values read from the csv file.
    values = []
 
    # This opens the input file as a csv and reads in the values.
    # Note: The first line on the input.txt is the number of nodes in the graph
    # The rest of the lines are the in the format: FromNode, ToNode, EdgeWeight
    with open('input.txt', 'r') as data:
        for line in csv.reader(data):
            values.append(line)

    # This first retrieves the number of nodes, and then the edges and
    # their corresponding weights.
    N = int(' '.join(map(str, values.pop(0))))
    edges = [tuple(x) for x in [list(map(int, value)) for value in values]]

    # This invokes Kruskal's magic.
    mst = kruskalAlgorithm(edges, N)

    # This calculates the total cost.
    total_cost = sum([pair[2] for pair in mst])

    # This is the output to the console.
    print("------------------------------------------------------------------")
    print("The Minimum Spanning Tree (MST) via Kruskal's Algorithm")
    print("Output Format: From-Node, To-Node, Edge-Weight")
    print("------------------------------------------------------------------")

    for s in mst:
        print("\t", ', '.join(str(item) for item in s))

    print("------------------------------------------------------------------")
    print("Total Cost of the MST:", total_cost)
    print("------------------------------------------------------------------")

# End of Script. ###################################################################