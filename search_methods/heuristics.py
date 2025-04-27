import numpy as np
from sokoban import Map
from scipy.optimize import linear_sum_assignment

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

def manhattan_heuristic_player(map: Map):
    h_value = manhattan_heuristic(map) 
    if h_value == 0:
        # We got to a good position
        return 0
    player_pos = (map.player.x, map.player.y)
    h_value += min(manhattan(player_pos, box) for box in map.positions_of_boxes)
    return h_value

# Heuristica 2: Hungarian matching pentru cutii și scopuri
def h_hungarian(map: Map):
    boxes = list(map.positions_of_boxes)
    goals = list(map.targets)
    cost_matrix = np.zeros((len(boxes), len(goals)))
    for i, box in enumerate(boxes):
        for j, goal in enumerate(goals):
            cost_matrix[i][j] = manhattan(box, goal)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return cost_matrix[row_ind, col_ind].sum()

def greedy_assign(map: Map):
    assigned = []
    h_value = 0
    for box in map.positions_of_boxes:
        distances = sorted(enumerate([manhattan(box, target) for target in map.targets]), key=lambda x : x[1])
        for elem in distances:
            if not elem[0] in assigned:
                assigned.append(elem[0])
                h_value += elem[1]
                break
    return h_value
