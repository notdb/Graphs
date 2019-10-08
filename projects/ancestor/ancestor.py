
def earliest_ancestor(ancestors, starting_node):
    pass

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
