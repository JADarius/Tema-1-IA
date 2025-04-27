from sokoban import Map

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def manhattan_heuristic(map: Map):
    h_value = 0
    for box in map.positions_of_boxes:
        h_value += min(manhattan(box, target) for target in map.targets)
    
    return h_value

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

def greedy_heuristic_player_pos(map: Map):
    h_value = greedy_assign(map) 
    if h_value == 0:
        # We got to a good position
        return 0
    player_pos = (map.player.x, map.player.y)
    h_value += min(manhattan(player_pos, box) for box in map.positions_of_boxes)
    return h_value


def is_corner(map: Map, pos):
    x, y = pos
    adj = [
        ((x-1, y), (x, y-1)),
        ((x-1, y), (x, y+1)),
        ((x+1, y), (x, y-1)),
        ((x+1, y), (x, y+1)),
    ]
    return any(a in map.obstacles and b in map.obstacles for a, b in adj)

def greedy_heuristic_player_pos_corner_penalty(map: Map):
    h_value = greedy_assign(map) 
    if h_value == 0:
        # We got to a good position
        return 0
    for box in map.positions_of_boxes:
        if is_corner(map, box):
            h_value += 100
    player_pos = (map.player.x, map.player.y)
    h_value += min(manhattan(player_pos, box) for box in map.positions_of_boxes)
    return h_value