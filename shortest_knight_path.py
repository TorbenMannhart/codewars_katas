# first working solution with networkx (not working on codewars)
# import matplotlib.pyplot as plt
import networkx as nx
def knight(p1, p2):
    start = translate(p1)
    end = translate(p2)
    G = nx.DiGraph()
    G.add_node(start)
    visited = [start]
    last_visited = [start]
    while end not in visited:
        next_moves = []
        for v in last_visited:
            for move in possible_moves(v):
                if move not in visited and move not in last_visited:
                    G.add_edge(v, move)
                    visited.append(move)
                    next_moves.append(move)
        last_visited = next_moves
    # nx.draw(G, with_labels=True)
    # plt.show()
    return len(nx.shortest_path(G, source=start, target=end)) - 1

def possible_moves(pos):
    """ returns a list of all possible moves """
    moves = []
    x = [1,2,2,1,-1,-2,-2,-1]
    y = [2,1,-1,-2,-2,-1,1,2]
    potential_moves = [(pos[0] + x[i], pos[1] + y[i]) for i in range(len(x))]
    return [move for move in potential_moves if move[0] >=0  and move[0] <= 7 and move[1] >=0 and move[1] <=7]

def translate(pos):
    """ translates input position into a tuple with two zero indexed integers"""
    t_pos = ('abcdefgh'.index(pos[0]), int(pos[-1])-1)
    return t_pos
""" ----------------------------------------------------------------------------------------------------------------- """

""" ----------------------------------------------------------------------------------------------------------------- """
# first working solution without nx
def knight(p1, p2):
    start = translate(p1)
    end = translate(p2)
    visited = [start]
    last_move = [((), start)]
    counter = 0
    while end not in visited:
        next_moves = []
        for v in last_move:
            for move in possible_moves(v):
                if move[1] not in visited and move not in last_move:
                    visited.append(move[1])
                    next_moves.append(move)
        last_move = next_moves
        counter +=1
    return counter

def possible_moves(last_move):
    """ returns a list of all possible moves """
    moves = []
    x = [1,2,2,1,-1,-2,-2,-1]
    y = [2,1,-1,-2,-2,-1,1,2]
    potential_moves = [(last_move[1][0] + x[i], last_move[1][1] + y[i]) for i in range(len(x))]
    return [(last_move[1], move) for move in potential_moves if move[0] >=0  and move[0] <= 7 and move[1] >=0 and move[1] <=7]

def translate(pos):
    """ translates input position into a tuple with two zero indexed integers"""
    t_pos = ('abcdefgh'.index(pos[0]), int(pos[-1])-1)
    return t_pos
""" ----------------------------------------------------------------------------------------------------------------- """


""" ----------------------------------------------------------------------------------------------------------------- """
# minor simplifications
def knight(p1, p2):
    start = translate(p1)
    end = translate(p2)
    last_move = [start]
    counter = 0
    while end not in last_move:
        next_moves = []
        for v in last_move:
            for move in possible_moves(v):
                if move not in last_move:
                    next_moves.append(move)
        last_move = next_moves
        counter +=1
    return counter

def possible_moves(last_move):
    """ returns a list of all possible moves """
    moves = []
    x = [1,2,2,1,-1,-2,-2,-1]
    y = [2,1,-1,-2,-2,-1,1,2]
    potential_moves = [(last_move[0] + x[i], last_move[1] + y[i]) for i in range(len(x))]
    return [move for move in potential_moves if move[0] >=0  and move[0] <= 7 and move[1] >=0 and move[1] <=7]

def translate(pos):
    """ translates input position into a tuple with two zero indexed integers"""
    t_pos = ('abcdefgh'.index(pos[0]), int(pos[-1])-1)
    return t_pos
""" ----------------------------------------------------------------------------------------------------------------- """
""" ----------------------------------------------------------------------------------------------------------------- """



arr =   [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], 
        ['a1', 'f4', 4], ['a1', 'f7', 5], ['b5', 'b6', 3], 
        ['a1', 'h8', 6], ['a1', 'h7', 5], ['c1', 'h8', 4]]
for item in arr:
    res = knight(item[0], item[1])
    if not res == item[-1]:
        print('****   ATTENTION! CALCULATED SOLUTION NOT EQUAL GIVEN SOLUTION   ****')
    print(f'number of steps from {item[0]} to {item[1]}?\ncalculated steps : {res}\nactual steps: {item[-1]}')
    if not res == item[-1]:
        print('*********************************************************************')

