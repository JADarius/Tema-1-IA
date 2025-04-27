import sys
from sokoban import Map
from search_methods import beam_search, ida_star, heuristics

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error: Insufficient arguments. Usage: ./main.py <algorithm> <input_file>")
        print("Possible algorithms: ida* beam-search")
        sys.exit(1)
    else:
        algorithm = sys.argv[1]
        input_file = sys.argv[2]

    map_from_yaml = Map.from_yaml(input_file)

    if algorithm == "ida*":
        solver = ida_star.IdaStar(map_from_yaml, heuristics.greedy_heuristic_player_pos_corner_penalty)
    elif algorithm == "beam-search":
        solver = beam_search.BeamSearch(map_from_yaml, heuristics.greedy_heuristic_player_pos, beam_width=10)
    else:
        print("Error: Invalid algorithm")
        print("Possible algorithms: ida* beam-search")
        sys.exit(2)

    solution = solver.solve()

    if isinstance(solution, list):
        for state in solution:
            print(state)
    else:
        print(solution)

    print(solver.explored_states)