from sokoban import (
    Box,
    DOWN,
    Map,
    Player
)
from search_methods import beam_search, ida_star, heuristics


if __name__ == '__main__':
    
    # Maps can be created through yaml files
    # Imi bag pula in sokoban-ul vostru
    map_from_yaml = Map.from_yaml('tests/medium_map2.yaml')

    ida_solver = ida_star.IdaStar(map_from_yaml, heuristics.greedy_assign)
    beam_search_solver = beam_search.BeamSearch(map_from_yaml, heuristics.manhattan_heuristic)
    solution = ida_solver.solve()

    if isinstance(solution, list):
        for state in solution:
            print(state)
    else:
        print(solution)