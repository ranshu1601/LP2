class MST:
    # Number of vertices in the graph
    V = int(input("Enter the vertex: "))

    # A utility function to find the vertex with minimum key value,
    # from the set of vertices not yet included in MST
    def minKey(self, key, mstSet):
        # Initialize min value
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent, graph):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", graph[i][parent[i]])

    # Function to construct and print MST for a graph represented using adjacency matrix representation
    def primMST(self, graph):
        # Array to store constructed MST
        parent = [None] * self.V

        # Key values used to pick the minimum weight edge in the cut
        key = [float('inf')] * self.V

        # To represent the set of vertices included in MST
        mstSet = [False] * self.V

        # Initialize all keys as infinite
        key[0] = 0  # Make key 0 so that this vertex is picked as the first vertex
        parent[0] = -1  # First node is always the root of MST

        # The MST will have V vertices
        for _ in range(self.V - 1):
            # Pick the minimum key vertex from the set of vertices not yet included in MST
            u = self.minKey(key, mstSet)

            # Add the picked vertex to the MST Set
            mstSet[u] = True

            # Update key value and parent index of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are not yet included in MST
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of u
                # mstSet[v] is False for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = graph[u][v]

        # Print the constructed MST
        self.printMST(parent, graph)


# Driver code
if __name__ == '__main__':
    """
    Let us create the following graph
            2    3
        (0)--(1)--(2)
        |   / \   |
       6|  8/   \5 |7
        | /     \ |
        (3)-------(4)
                  9
    """
    t = MST()
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    # Print the solution
    t.primMST(graph)
