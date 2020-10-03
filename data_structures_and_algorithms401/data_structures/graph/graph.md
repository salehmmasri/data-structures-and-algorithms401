# Graphs
- Introduction to Graphs data structure

# Challenge
- Using a graphs data structure, methods will add nodes, add edges'

# Approach & Efficiency
- Big O of get_edges is O(n squared)

# API
- AddEdge()
    - Adds a new edge between two nodes in the graph
    - Include the ability to have a “weight”
    - Takes in the two nodes to be connected by the edge
- AddNode()
   -  Adds a new node to the graph
    - Takes in the value of that node
    - Returns the added node
- GetNodes()
    - Returns all of the nodes in the graph as a collection (set, list, or similar)
- GetNeighbors()
    - Returns a collection of edges connected to the given node
    - Takes in a given node
    - Include the weight of the connection in the returned collection
- Size()
    - Returns the total number of nodes in the graph