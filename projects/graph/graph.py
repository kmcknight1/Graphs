"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # use a queue
        # add node(starting_vertex) to queue
        # dequeue node, add node to visited, queue neighbors
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)  # enqueue starting_vertex
        visited.add(starting_vertex)  # add starting_vertex to visited

        while queue.size() > 0:
            u = queue.dequeue()  # item popped at index 0
            print(u)  # print that item
            for v in self.get_neighbors(u):  # loop through the neighbors
                if v not in visited:
                    visited.add(v)  # add each one to the visited set
                    queue.enqueue(v)  # enqueue each one (append to queue)

    def dft(self, starting_vertex):
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        visited.add(starting_vertex)

        while stack.size() > 0:
            u = stack.pop()  # item popped at last index
            print(u)  # print that item
            for v in self.get_neighbors(u):
                if v not in visited:
                    visited.add(v)
                    stack.push(v)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        visited.add(starting_vertex)

        # make a function to call recursively
        def dft_print(starting_vertex):
            print(starting_vertex)  # print the node
            for v in self.get_neighbors(starting_vertex):  # get the neighbors
                if v not in visited:
                    visited.add(v)  # add them to visited
                    # recursively pass each neighbor into the function
                    dft_print(v)

        dft_print(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        path = [starting_vertex]
        queue.enqueue(path)

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        path = [starting_vertex]
        stack.push(path)

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dft_helper(vertex, visited):

            if vertex == destination_vertex:
                return [vertex]

            if vertex not in visited:
                visited.add(vertex)

                if self.get_neighbors(vertex) is None:
                    return None

                for neighbor in self.get_neighbors(vertex):
                    path = dft_helper(neighbor, visited)
                    if path:
                        return [vertex, *path]

        visited = set()
        path = dft_helper(starting_vertex, visited)

        return path


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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
