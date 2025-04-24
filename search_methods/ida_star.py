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

    def solve(self):
        def df(start: Map, g, limit):
            f = g + self.heuristic(start)
            if f > limit:
                return f
            if start.is_solved():
                return self.path(start)
            min = INSUCCESS
            for state in start.get_neighbours():
                if not state in self.path(start):
                    self.parents[state] = start
                    temp = df(state, g + 1, limit)
                    if isinstance(temp, list):
                        return temp
                    elif (temp != INSUCCESS and min == INSUCCESS) or (temp < min):
                        min = temp
            return min

        limit = self.heuristic(self.start)
        state = self.start
        self.parents[self.start] = None
        while True:
            temp = df(state, 0, limit)
            if isinstance(temp, list):
                return temp
            if temp == INSUCCESS:
                return temp
            limit = temp



    def path(self, state: Map):
        sol = [state]
        while self.parents[state] != None:
            state = self.parents[state]
            sol.append(state)
        return sol
