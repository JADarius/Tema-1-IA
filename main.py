import sys
from sokoban import Map, gif
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
        if algorithm == "ida*":
            # To avoid crashes when naming the files
            algorithm = "ida_star"
        gif.save_images(solution, f"images/{input_file}_{algorithm}_steps")
        gif.create_gif(f"images/{input_file}_{algorithm}_steps", f"{input_file}_{algorithm}_demo", "images")
        for state in solution:
            print(state)
    else:
        print(solution)

    print(f"Elapsed time: {solver.elapsed_time} seconds")
    print(f"Explored states: {solver.explored_states}")