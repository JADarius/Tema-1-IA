import numpy as np
from sokoban import Map

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def is_corner(pos, walls):
    """Verifică dacă o poziție e într-un colț (două ziduri adiacente)."""
    x, y = pos
    adj = [
        ((x-1, y), (x, y-1)),
        ((x-1, y), (x, y+1)),
        ((x+1, y), (x, y-1)),
        ((x+1, y), (x, y+1)),
    ]
    return any(a in walls and b in walls for a, b in adj)

def manhattan_heuristic(map: Map):
    h_value = 0
    for box in map.positions_of_boxes:
        h_value += min(manhattan(box, target) for target in map.targets)
    
    return h_value

# # Heuristica 1: suma celor mai apropiate distanțe Manhattan box -> goal
# def h_manhattan(state):
#     boxes = state.boxes
#     goals = state.goals
#     total = 0
#     for box in boxes:
#         total += min(manhattan(box, goal) for goal in goals)
#     return total

# # Heuristica 2: Hungarian matching pentru cutii și scopuri
# def h_hungarian(state):
#     boxes = list(state.boxes)
#     goals = list(state.goals)
#     cost_matrix = np.zeros((len(boxes), len(goals)))
#     for i, box in enumerate(boxes):
#         for j, goal in enumerate(goals):
#             cost_matrix[i][j] = manhattan(box, goal)
#     row_ind, col_ind = linear_sum_assignment(cost_matrix)
#     return cost_matrix[row_ind, col_ind].sum()

# # Heuristica 3: Hungarian + penalizare pentru cutii blocate în colț
# def h_blocked_penalty(state):
#     base = h_hungarian(state)
#     penalty = 0
#     for box in state.boxes:
#         if box not in state.goals and is_corner(box, state.walls):
#             penalty += 100  # mare, ca să fie fail-fast
#     return base + penalty
