import time
from search_methods import solver
from sokoban import Map

DONE = -1
INSUCCESS = float("inf")

class IdaStar(solver.Solver):
    def __init__(self, map: Map, heuristic):
        super().__init__(map)
        self.heuristic = heuristic
        self.start = self.map
        self.parents = {}
        self.elapsed_time = 0
        self.explored_states = 0

    def solve(self):
        def df(start: Map, g, limit):
            self.explored_states += 1
            f = g + self.heuristic(start)
            if f > limit:
                return f
            if start.is_solved():
                return self.path(start)[::-1]

            if start in transposition_table and transposition_table[start] <= g:
                return INSUCCESS
            else:
                transposition_table[start] = g


            min = INSUCCESS
            for state in start.get_neighbours():
                if not state in visited:
                    self.parents[state] = start
                    visited.add(state)
                    temp = df(state, g + 1, limit)
                    visited.remove(state)
                    if isinstance(temp, list):
                        return temp
                    elif temp != INSUCCESS and (min == INSUCCESS or temp < min):
                        min = temp
            return min

        start_time = time.time()
        limit = self.heuristic(self.start)
        state = self.start
        self.parents[self.start] = None
        visited = set()
        while True:
            transposition_table = {}
            visited.add(self.start)
            temp = df(state, 0, limit)
            if isinstance(temp, list):
                self.elapsed_time = time.time() - start_time
                return temp
            if temp == INSUCCESS:
                self.elapsed_time = time.time() - start_time
                return temp
            limit = temp

    def path(self, state: Map):
        sol = [state]
        while self.parents[state] != None:
            state = self.parents[state]
            sol.append(state)
        return sol
