# Words - vertex
# letters different - edges (part)
# shortest transformation sequence - path/bfs
# dictionary - list of vertexes
# beginWord - starting vertex
# EndWord - ending vertex
# No duplicates - use a set()
# same length - edges (part)


f = open('words.txt', 'r')
words = f.read().split('\n')

word_set = set()
for word in words:
    word_set.add(word.lower())

# find/create all nodes/edges for words with one letter different
# replaces entry in the adjaency list for that node
def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
                   for letter in list("abcdefghijklmnopqrstuvwxyz"):
                       temp_word = list(string_word)
                       temp_word[i] = letter
                       w = "".join(temp_word)
                       if w != word and w in word_set:
                           neighbors.append(w)

    return neighbors

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def find_word_ladder(beginWord, endWord):
    qq = Queue()
    visited = set()
    qq.enqueue([beginWord])

    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1] # Vertex is our word
        if vertex not in visited:
            # Here's where we do the thing!
            if vertex == endWord:
                return path
            visited.add(vertex)
            for new_vert in get_neighbors(vertex):
                new_path = list(path)
                new_path.append(new_vert)
                qq.enqueue(new_path)

                
print(get_neighbors('boll'))
print(find_word_ladder('sail', 'boat'))
