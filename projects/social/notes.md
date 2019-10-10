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

Something about going into the function to see what type the function arguments
take when they could be listed in the actual function parameter up front to save
some time

sg.users doesn't print the users it's stored as some weird stuff. Taking a look

So add user takes a string for a name, and then automatically creates an
id. addfriendship uses that id to make the friendship. As expected, it does make
a bidirectional (1,2), (2,1) link automatically, so we don't have to worry about
that aspect when generating friends. 

As far as populatingGraph goes, numUsers should be used to generate some sort of
list. for example 10, would make 10 users from 1-10, and then average
friendships will create a list of friendships between that user and another
user. We have to be careful that the pairs are unique for friendships. For
example user 1 could be friends with user 2,3,4, but when we go to create 2's
friendships, we have to check if 2 is already friends with 1, or essentially,
take 2 out of the bag. We can do this with some sort of bag setup like say you
have two arrays, [] and [1,2,3,4]. Pull 1 out so you have [1] and [2,3,4], now
pull 2 out and use 2 to make the relationships from the remaining balls, [3,4] 

gonn have to think about this some more, because what happens with 3, 1 is never
friends with 3, so does that mean we can put 1 back in the bag? and that the
relationships only exist for a set of balls at a time?

We can make a list of all the friendship combinations and remove
duplicates. That should work.

Added that now we need to work on the populate graph function
