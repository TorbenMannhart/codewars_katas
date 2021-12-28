# first working solution
import itertools
def solve_puzzle (clues):
    clue_dic = {}
    clue_dic['rows'] =  [[clues[15-i], clues[4+i]] for i in range(4)]
    clue_dic['cols'] = [[clues[i], clues[11-i]] for i in range(4)] 
    all_combinations = list(itertools.permutations([1,2,3,4], 4))
    row_clues_included = []
    for i in range(4):
        left_clue = clue_dic['rows'][i][0]
        right_clue = clue_dic['rows'][i][-1]
        row_clues_included.append([r for r in all_combinations if clue_is_true(r, left_clue, right_clue)])  

    all_combinations_of_row_clues_included = list(itertools.product(*row_clues_included))
    inverted = invert_list_of_matrices(all_combinations_of_row_clues_included)
    all_clues_included = []
    for j, guess in enumerate(all_combinations_of_row_clues_included):
        row = []
        for i in range(4):
            left_clue = clue_dic['cols'][i][0]
            right_clue = clue_dic['cols'][i][-1]
            if clue_is_true(inverted[j][i], left_clue, right_clue):
                row.append(all_combinations_of_row_clues_included[j][i])
        if len(row) == 4:
            all_clues_included.append(row)

    inverted_all_clues_included = invert_list_of_matrices(all_clues_included)
    result = ()
    for i, guess in enumerate(inverted_all_clues_included):
        valid = []
        for j in range(4):
            if each_number_only_once(guess[j]):
                valid.append(all_clues_included[i][j])
        if len(valid) == 4:
            result = valid
    return tuple(result)
    
def each_number_only_once(col):
    if 1 in col and 2 in col and 3 in col and 4 in col:
        return True
    return False

def clue_is_true(row, left_clue, right_clue):
    left_sum = 1
    right_sum = 1
    highest = row[0]
    for i in range(1, 4):
        if row[i] > highest:
            highest = row[i]
            left_sum += 1
    highest = row[-1]
    for i in range(2, -1, -1):
        if row[i] > highest:
            highest = row[i]
            right_sum += 1

    if ((left_sum == left_clue and right_sum == right_clue) or 
        (left_clue == 0 and right_clue == 0) or 
        (left_clue == 0 and right_sum == right_clue) or 
        (right_clue == 0 and left_sum == left_clue)):
        return True
    return False

def invert_list_of_matrices(list_of_matrices):
    inverted = []
    for matrix in list_of_matrices:
        inverted.append(list(zip(*matrix)))
    return inverted
        


# codewars solution (with own comments)
from itertools import permutations, chain

def solve_puzzle(clues):
    size = 4
    for poss in permutations(permutations(range(1, size+1), size), size): # can use generator directly in for loop (space efficient)
        for i in range(size):
            if len(set(row[i] for row in poss)) < size: # set object only allows unique values: {1,2,2,3} == {1,2,3}
                break
        else: # for ... else : used twice in this method. here if for didnt break, else is executed.
            cols_top = [[row[i] for row in poss] for i in range(size)] # here all directions of the poss matrix is saved in different lists
            rows_right = [list(reversed(row)) for row in poss]
            cols_btm = [[row[i] for row in reversed(poss)] for i in reversed(range(size))]
            rows_left = list(reversed(poss)) # reversed because clues are numbered from top to right to bottom to left -> first clue for left is its last row
            for i, row in enumerate(chain(cols_top, rows_right, cols_btm, rows_left)): # 'chain' chains all iterables and treats them as one list
                if not clues[i]:
                    continue
                visible = 0
                for j, v in enumerate(row):
                    visible += v >= max(row[:j+1]) # very elegant solution to how many are visible
                if visible != clues[i]:
                    break
            else: # seconds for ... else ... : if for loop doesnt break poss is returned
                return poss

clues = (
( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 ),
( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
)

outcomes = (
( ( 1, 3, 4, 2 ),       
  ( 4, 2, 1, 3 ),       
  ( 3, 4, 2, 1 ),
  ( 2, 1, 3, 4 ) ),
( ( 2, 1, 4, 3 ), 
  ( 3, 4, 1, 2 ), 
  ( 4, 2, 3, 1 ), 
  ( 1, 3, 2, 4 ) )
)

a = solve_puzzle(clues[0]) # == outcomes[0]
b = solve_puzzle(clues[1]) # == outcomes[1]

print(a)
print(b)
