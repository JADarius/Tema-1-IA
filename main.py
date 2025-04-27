from sokoban import (
    Box,
    DOWN,
    Map,
    Player,
    gif,
)
from search_methods import beam_search, ida_star, heuristics


if __name__ == '__main__':
    
    # Maps can be created through yaml files
    map_from_yaml = Map.from_yaml('tests/super_hard_map1.yaml')

    ida_solver = ida_star.IdaStar(map_from_yaml, heuristics.manhattan_heuristic_player)
    beam_search_solver = beam_search.BeamSearch(map_from_yaml, heuristics.manhattan_heuristic_player)
    solution = beam_search_solver.solve()

    if isinstance(solution, list):
        gif.save_images(solution, "images/super_hard_map1")
        gif.create_gif("images/super_hard_map1", "super_hard_map1_demo", "images")
        for state in solution:
            print(state)
    else:
        print(solution)