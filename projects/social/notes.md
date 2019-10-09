## 1. Generating Users and Friendships

So we need to fill in a function populateGraph(numUsers, avgFriendships) to
generate users for our graph essentially.

They've given us addUser and addFriendship functions that allow us to add users
to the graph as well as creating a friendship. A friendship is a bidirectional
link between two vertices (or nodes) in the graph. For example, Node 1 is 1 and
Node 2 is 2.

Their link or edge would be (1,2) it's bidirectional, so (2,1) shouldu be the
same thing. It remains to be seen if the function is adding the reverse
automatically.  

First order of business is to add two users and test the functions to see what
the friendship link actually looks like.
