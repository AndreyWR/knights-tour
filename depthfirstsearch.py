from collections import defaultdict
from pythonds.graphs import Graph

class profundidade:
    def __init__(self, posicaox, posicaoy, tamtabuleiro):
        self.posicaox = posicaox
        self.posicaoy = posicaoy
        self.tamtabuleiro = tamtabuleiro

    # Adiciona os vértices no grafo
    def add_edge(self, graph, vertex_a, vertex_b):
        graph[vertex_a].add(vertex_b)
        graph[vertex_b].add(vertex_a)

    #Constrói o Grafo
    def build_graph(self):
        graph = defaultdict(set)
        for row in range(self.tamtabuleiro):
            for col in range(self.tamtabuleiro):
                for to_row, to_col in self.legal_moves_from(self.posicaox, self.posicaoy):
                    self.add_edge(graph, (self.posicaox, self.posicaoy), (to_row, to_col))

                self.posicaoy += 1
                if self.posicaoy == self.tamtabuleiro:
                    self.posicaoy = 0
            self.posicaox += 1
            if self.posicaox == self.tamtabuleiro:
                self.posicaox = 0
        return graph

    # Verifica quais os movimentos legais no tabuleiro
    def legal_moves_from(self, row, col):

        MOVE_OFFSETS = (
                      (-1, -2), ( 1, -2),
            (-2, -1),                     ( 2, -1),
            (-2,  1),                     ( 2,  1),
                      (-1,  2), ( 1,  2),
        )

        for row_offset, col_offset in MOVE_OFFSETS:
            move_row, move_col = row + row_offset, col + col_offset
            if 0 <= move_row < self.tamtabuleiro and 0 <= move_col < self.tamtabuleiro:
                yield move_row, move_col

    def first_true(self, sequence):
        for item in sequence:
            if item:
                return item
        return None

    # Encontra a solução no tabuleiro
    def find_solution_for(self, heuristic=lambda graph: None):
        graph = self.build_graph()
        total_squares = self.tamtabuleiro * self.tamtabuleiro

        def traverse(path, current_vertex):
            if len(path) + 1 == total_squares:
                # incluindo o quadrado atual, nós visitamos cada quadrado,
                # então retorna o caminho como uma solução
                return path + [current_vertex]

            yet_to_visit = graph[current_vertex] - set(path)
            if not yet_to_visit:

                # sem vizinhos não-visitados, então é um beco sem saída
                return False

            # tenta todos os caminhos válidos deste ponto
            next_vertices = sorted(yet_to_visit, key = heuristic(graph))
            return self.first_true(traverse(path + [current_vertex], vertex)
                              for vertex in next_vertices)

        # tenta encontrar uma solução de qualquer quadrado no tabuleiro
        return self.first_true(traverse([], starting_vertex)
                          for starting_vertex in graph)
