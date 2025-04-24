from sokoban import (
    Box,
    DOWN,
    Map,
    Player
)
from search_methods import ida_star, heuristics


if __name__ == '__main__':
    
    # Maps can be created through yaml files
    map_from_yaml = Map.from_yaml('tests/easy_map1.yaml')

    ida_solver = ida_star.IdaStar(map_from_yaml, heuristics.manhattan_heuristic)
    solution = ida_solver.solve()

    if isinstance(solution, list):
        for state in solution:
            print(state)
    else:
        print(solution)

    # plot_flag = False

    # if plot_flag:
    #     crt_map.plot_map()
    # else:
    #     print(crt_map)
    #     print(f"Is solved: {crt_map.is_solved()}")
    #     print("Neighbours:")
    #     for neighbour in crt_map.get_neighbours():
    #         print(neighbour)
