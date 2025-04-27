import random
import time
from search_methods import solver
from sokoban import Map

class BeamSearch(solver.Solver):
    def __init__(self, map: Map, heuristic, beam_width=5, max_iters=10000):
        super().__init__(map)
        self.heuristic = heuristic
        self.start = self.map
        self.parents = {}
        self.beam_width = beam_width
        self.max_iters = max_iters
        self.elapsed_time = 0
        self.explored_states = 0

    def solve(self):
        start_time = time.time()
        random.seed(0)
        frontier = [(self.heuristic(self.start), self.start, [self.start])]
        visited = set()
        visited.add(self.start)

        for _ in range(self.max_iters):
            next_frontier = []
            for _, state, path in frontier:
                self.explored_states += 1
                if state.is_solved():
                    self.elapsed_time = time.time() - start_time
                    return path
                for next_state in state.get_neighbours():
                    if next_state not in visited:
                        score = self.heuristic(next_state)
                        next_frontier.append((score, next_state, path + [next_state]))
                        visited.add(next_state)

            if not next_frontier:
                self.elapsed_time = time.time() - start_time
                return None

            next_frontier.sort()
            frontier = next_frontier[:self.beam_width]

        self.elapsed_time = time.time() - start_time
        return None
