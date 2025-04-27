import matplotlib.pyplot as plt
from sokoban import (
    Map,
)
from search_methods import beam_search, ida_star, heuristics

easy_map = Map.from_yaml('tests/easy_map2.yaml')
medium_map = Map.from_yaml('tests/medium_map2.yaml')
hard_map = Map.from_yaml('tests/hard_map2.yaml')

ida_solver_easy = ida_star.IdaStar(easy_map, heuristics.greedy_heuristic_player_pos_corner_penalty)
beam_search_solver_easy = beam_search.BeamSearch(easy_map, heuristics.greedy_heuristic_player_pos, beam_width=10)

ida_solver_medium = ida_star.IdaStar(medium_map, heuristics.greedy_heuristic_player_pos_corner_penalty)
beam_search_solver_medium = beam_search.BeamSearch(medium_map, heuristics.greedy_heuristic_player_pos, beam_width=10)

ida_solver_hard = ida_star.IdaStar(hard_map, heuristics.greedy_heuristic_player_pos_corner_penalty)
beam_search_solver_hard = beam_search.BeamSearch(hard_map, heuristics.greedy_heuristic_player_pos, beam_width=10)

ida_solver_easy.solve()
ida_solver_medium.solve()
ida_solver_hard.solve()
beam_search_solver_easy.solve()
beam_search_solver_medium.solve()
beam_search_solver_hard.solve()

values_easy = [ida_solver_easy.elapsed_time, beam_search_solver_easy.elapsed_time]
values_medium = [ida_solver_medium.elapsed_time, beam_search_solver_medium.elapsed_time]
values_hard = [ida_solver_hard.elapsed_time, beam_search_solver_hard.elapsed_time]

names = ['IDA*', "Beam Search"]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))

ax1.bar(names, values_easy, color='skyblue', edgecolor='black')
ax1.set_title("easy_map2.yaml")
ax1.set_xlabel("Algorithm")
ax1.set_ylabel("Time (seconds)")
ax1.grid(axis='y', linestyle='--', alpha=0.6)

ax2.bar(names, values_medium, color='lightgreen', edgecolor='black')
ax2.set_title("medium_map2.yaml")
ax2.set_xlabel("Algorithm")
ax2.set_ylabel("Time (seconds)")
ax2.grid(axis='y', linestyle='--', alpha=0.6)

ax3.bar(names, values_hard, color='lightgreen', edgecolor='black')
ax3.set_title("hard_map2.yaml")
ax3.set_xlabel("Algorithm")
ax3.set_ylabel("Time (seconds)")
ax3.grid(axis='y', linestyle='--', alpha=0.6)

plt.suptitle("Elapsed Time", fontsize=14)
plt.tight_layout()
plt.savefig("elapsed_time.png")