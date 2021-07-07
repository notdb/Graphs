# I get that we have parent child pairs
# Each node is assigned a unique integer identifier

# I don't understand if the relationships are directed or not
# The directions imply they are
# for example in the picture, 6 should be a child of 3 and 5
# 10 is a child of 1
# The test case is the same as the example, so we should be able
# to make something based on the example case
# So the list goes from oldest to youngest. It's called the earliest ancestor, but basically you're  looking for the oldest member of the family whose directly related to you. It's weird looking at the bottom of the graph and going upwards, but that's where we're starting.

# I think it'd make more sense to start at the top and work our way down

# Realistically, it wouldn't make a difference

# I suppose this is a directed graph then if the arrows only point up or down depending on how you look at it.

# Regardless, doing this with a DFS seems to make more sense because the answer is more likely to be at the end of a branch than overall with a breadth first search.

# Going to take a look at dfs vs bfs and see which one looks easier to implement

# Both of those scour the entire tree

# this will be easier if I can find a way to identify directions from how they were inputed

# the problem is the graph isn't directed, or at least I don't know if it is

# if it was, then you could design a traversal to never go backwards, keep track of all the possible paths, and pick the longest path

# need to figure out a way to determine the direction
# without the picture it's near impossible to tell whose who
# granted they told us in the description
# so we should be able to tell an algorithm that somehow


# we do know all the children are on the right and the parents are on the left

# that's something

# that might be all we need to build everything up

# got it

# so you want to take the input, loop through the array to see if it's listed as a child in any of the tuples

# every time it's listed you make a "new path" with the input being the parent of the tuple of the last input

# every time you make a new path, you keep track of it, and then at the end you find the longest path and output the final number

# can probably be done recursively, may or may not attempt

# also looks slimilar to a DFS like I said earlier

def earliest_ancestor(ancestors, starting_node):
    # loop through the ancestors and print each ancestor whose tuple contains the starting node
    newList3 = []
    def new_stuff(ancestors, starting_node):
        newList = []
        newList.append(starting_node)
        newList2 = []
        newList2.append(starting_node)
        num = 0
        for (x, y) in ancestors:
            if y is starting_node:
            #print(True, (x, y))
                new_stuff([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], x)
                #print(x)
                newList.append(x)
            else:
                newList.append(y)
        
        newList2.append(newList)
        return newList3.append(newList2[0])
    new_stuff(ancestors, starting_node)
    if newList3[0] is starting_node:
        newList3[0] = -1
    return newList3[0]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

#earliest_ancestor(test_ancestors, 1)

def earliest_ancestor2(ancestors, starting_node):
    class Graph:
        def __init__(self):
            self.vertices = {}
            self.visited2 = set()
        def add_vertex(self, vertex):
            self.vertices[vertex] = set()
        
        def add_edge(self, v1, v2):
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)
            else:
                raise IndexError("Can not create edge based on given vertices!")
    # create new graph
    graph = Graph()
    newSet = set()

    # add vertices
    for (x, y) in ancestors:
         newSet.add(x)
         newSet.add(y)
    for thing in newSet:
        graph.add_vertex(thing)
    # add edges
    for (x, y) in ancestors:
        graph.add_edge(x, y)
        
    def dft_recursive(starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if len(graph.visited2) == len(graph.vertices):
            return 0
        if starting_vertex not in graph.visited2:
            graph.visited2.add(starting_vertex)
            if starting_vertex is None:
                pass
            else:
                print(starting_vertex)
            for next_vert in graph.vertices[starting_vertex]:
                dft_recursive(next_vert)
        else:
            pass

    dft_recursive(starting_node)

earliest_ancestor2(test_ancestors, 6)         
