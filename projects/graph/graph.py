"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited2 = set()
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices!")
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        BFT Pseudocode
        Create a queue
        Create list of visited nodes
        Put starting node in the queue
        While: queue not empty
        Pop first node out of queue
        If not visited
        Mark as visited
        Get adjacent edges and add to list
        Goto top of loop

        """
        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        while que.size() > 0:
            vertex = que.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    que.enqueue(next_vert)

        pass  # TODO
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        Make a stack
        Make visited list
        Add first node to stack
        While stack not empty:
        Pop top item
        if not visited:
        Mark as visited
        Get adjacent and add to stack

        """
        questack = Stack()
        visited = set()
        questack.push(starting_vertex)
        while questack.size() > 0:
            vertex = questack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    questack.push(next_vert)
                    #print(f'{next_vert} aaaaAAAA')
                    #print(visited)
                    #print(self.vertices)
                    #print(len(self.vertices))
                    #print(len(visited))
                    
    
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if len(self.visited2) == len(self.vertices):
            return 0
        if starting_vertex not in self.visited2:
            self.visited2.add(starting_vertex)
            if starting_vertex is None:
                pass
            else:
                print(starting_vertex)
            for next_vert in self.vertices[starting_vertex]:
                self.dft_recursive(next_vert)
        else:
            pass
            
        # figure out exit condition (when are we finished)
        # call itself, simplest case
        # I want to say all dft_recursive should be doing is checking if it can go deeper, when it can't, mark node as visisted and pass it up.
        # So you'd start, go deeper, go deeper, go deeper, can't go deeper, mark visited, go back, mark visited, go back, mark visited, done.
        # Something like that. dft_recursive is essentially go deeper, if not, mark visited and grab the last thing off the call stack.
        # What's go deeper?
        # Going deeper is pushing it into visited if it's not visited
        # exit condition can be when visited and self.vertices have the same length
        # we may not need the Stack() data structure because it (recursion abuses the call stack anyways)

                
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        finalList = []
        newList = []
        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        while que.size() > 0:
            vertex = que.dequeue()
            if vertex is destination_vertex:
                #newList.append(vertex)
                #print(newList)
                dVert = destination_vertex
                #print(dVert)
                newList.reverse()
                for listItem in newList:
                    #print(f'{newList} AAA')
                    #print(f'{listItem} BBB')
                    if dVert in self.vertices[listItem]:
                        dVert = listItem
                        finalList.append(listItem)
                        #print(f'{dVert} hello')
                    else:
                        #print(f'{newList[0]} test')
                        dVert
                        #newList.pop(0)
                finalList.reverse()
                finalList.append(destination_vertex)
                return finalList
            if vertex not in visited:
                visited.add(vertex)
                newList.append(vertex)
                #print(vertex)
                for next_vert in self.vertices[vertex]:
                           que.enqueue(next_vert)
        
                    # we need to create some sort of branching list
                    # the problem is storage
                    # if it branches once thats fine
                    # if it's more than once say 4 times
                    # what happens?
                    # Once you find the destination
                    # we have a list of all the points in the dictionary
                    # take the list we used to build up the initial graph
                    # save the starting point, reverse the list
                    # take the first number (the destination), check the remaining numbers in the list to see if it's found in one of their values
                    # add the current destination to a new list
                    # the found number becomes the new destination, and you repeat until the new destination and the starting vertex match

                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
   # print("starting dft")
   #graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #print('starting bft')
    #graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #print('starting dft_recursive')
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('starting bfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
