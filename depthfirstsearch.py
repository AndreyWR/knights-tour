from collections import defaultdict
from pythonds.graphs import Graph

class Depth:
    def __init__(self, positionx, positiony, boardsize):
        self.positionx = positionx
        self.positiony = positiony
        self.boardsize = boardsize

    # Add the vertices to the graph
    def add_edge(self, graph, vertex_a, vertex_b):
        graph[vertex_a].add(vertex_b)
        graph[vertex_b].add(vertex_a)

    # Build the graph
    def build_graph(self):
        graph = defaultdict(set)
        for row in range(self.boardsize):
            for col in range(self.boardsize):
                for to_row, to_col in self.legal_moves_from(self.positionx, self.positiony):
                    self.add_edge(graph, (self.positionx, self.positiony), (to_row, to_col))

                self.positiony += 1
                if self.positiony == self.boardsize:
                    self.positiony = 0
            self.positionx += 1
            if self.positionx == self.boardsize:
                self.positionx = 0
        return graph

    # Check what are the legal moves on the board
    def legal_moves_from(self, row, col):

        MOVE_OFFSETS = (
                      (-1, -2), ( 1, -2),
            (-2, -1),                     ( 2, -1),
            (-2,  1),                     ( 2,  1),
                      (-1,  2), ( 1,  2),
        )

        for row_offset, col_offset in MOVE_OFFSETS:
            move_row, move_col = row + row_offset, col + col_offset
            if 0 <= move_row < self.boardsize and 0 <= move_col < self.boardsize:
                yield move_row, move_col

    def first_true(self, sequence):
        for item in sequence:
            if item:
                return item
        return None

    # Find the solution on the board
    def find_solution_for(self, heuristic=lambda graph: None):
        graph = self.build_graph()
        total_squares = self.boardsize * self.boardsize

        def traverse(path, current_vertex):
            if len(path) + 1 == total_squares:
                # Including the current square, we visit each square,
                # then return the path as a solution.
                return path + [current_vertex]

            yet_to_visit = graph[current_vertex] - set(path)
            if not yet_to_visit:

                # No unvisited neighbors, so it's a dead end.
                return False

            # Try all valid paths from this point
            next_vertices = sorted(yet_to_visit, key = heuristic(graph))
            return self.first_true(traverse(path + [current_vertex], vertex)
                              for vertex in next_vertices)

        # Try to find a solution of any square on the board.
        return self.first_true(traverse([], starting_vertex)
                          for starting_vertex in graph)
