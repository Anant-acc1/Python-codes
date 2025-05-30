'''
sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku = [[4, 3, 5, 2, 6, 9, 7, 8, 0],
          [6, 8, 2, 5, 7, 1, 4, 0, 3],
          [1, 9, 7, 8, 3, 4, 0, 6, 2],
          [8, 2, 6, 1, 9, 0, 3, 4, 7],
          [3, 7, 4, 6, 0, 2, 9, 1, 5],
          [9, 5, 1, 0, 4, 3, 6, 2, 8],
          [5, 1, 0, 3, 2, 6, 8, 7, 4],
          [2, 0, 8, 9, 5, 7, 1, 3, 6],
          [0, 6, 3, 4, 1, 8, 2, 5, 9]]

sudoku = [[0, 0, 0, 0, 5, 0, 0, 7, 0],
          [0, 5, 7, 2, 0, 8, 1, 0, 0],
          [8, 0, 0, 0, 7, 4, 6, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1],
          [0, 3, 0, 0, 0, 0, 4, 2, 0],
          [0, 1, 9, 6, 0, 0, 0, 0, 3],
          [0, 0, 0, 0, 1, 0, 0, 0, 0],
          [3, 0, 0, 7, 0, 2, 9, 0, 0],
          [0, 7, 5, 4, 0, 0, 3, 0, 0]]
'''

sudoku = []
boxes = []
#returns a box
def get_box (row, col):
    box: list[int] = []
    for i in range(3 * (row // 3), 3 * (row // 3 + 1)):
        for j in range(3 * (col // 3), 3 * (col // 3 + 1)):
            box.append(sudoku[i][j])
    return box
#makes a list of elements in boxes
def get_boxes():
    boxes = []
    for i in range(1, 10, 3):
        for j in range(1, 10, 3):
            boxes.append(get_box(i, j))
    return boxes
#takes the transpose of a matrix
def transpose (m):
    m_trans = [[row[i] for row in m] for i in range(len(m[0]))]
    return m_trans
#makes a list of all the blank locations in the sudoku
def get_blanks(sudoku):
    blanks = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                blanks.append((i, j))
    return blanks
#makes a dictionary of all possible values an empty cell may take [location] -> [possible values]
def get_possibilities():
    possible = {}
    for (row, col) in blanks:
        temp_r = set()
        temp_c = set()
        temp_b = set()
        box_index = 3 * (row // 3) + col // 3
        blanks_in_boxes[box_index].append((row, col))
        for i in range(1, 10):
            if i not in sudoku[row]:
                temp_r.add(i)
            if i not in sudoku_t[col]:
                temp_c.add(i)
            if i not in boxes[box_index]:
                temp_b.add(i)
        possible[(row, col)] = list(temp_b.intersection(temp_c, temp_r))
    return possible
#makes a dictionary of the number of occurrences of a number in a box [number] -> [total repeats]
def get_occurrences():
    occur = {}
    for position in blanks_in_boxes[box]:
        for p in possible[position]:
            try:
                occur[p] += 1
            except KeyError:
                occur[p] = 1
    return occur
#check if sudoku is solved
def check(sudoku):
    total = 0
    for row in sudoku:
        # print(row)
        total += sum(row)
    return total == 405

for i in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)

solved = False
iteration = 1

while not solved:
    boxes = get_boxes() # makes 9 boxes, each is indexed from 0 to 8
    sudoku_t = transpose(sudoku) # Treats the sudoku like a matrix and makes a transpose of it NOTE: THIS DOESN'T CHANGE THE SOLUTION
    blanks = get_blanks(sudoku) # Gets empty spaces(0 entries) in the sudoku
    blanks_in_boxes = {key : [] for key in range(9)} # Makes a dictionary with box-id as key and list of empty spaces in the box as values
    possible = get_possibilities() # Gets all possible values of an empty cell

    '''
    for box in blanks_in_boxes:
        print(f"{box}: {blanks_in_boxes[box]}")
        for position in blanks_in_boxes[box]:
            print(f'{position}: {possible[position]}')
    ''' #check before updating values

    for box in blanks_in_boxes:
        for position in blanks_in_boxes[box]:
            if len(possible[position]) == 1:
                filled = possible[position].pop()
                sudoku[position[0]][position[1]] = filled
                del possible[position]
                blanks_in_boxes[box].remove(position)
                for p in blanks_in_boxes[box]:
                    if filled in possible[p]:
                        possible[p].remove(filled)

        occurrences = get_occurrences()

        for val in occurrences:
            if occurrences[val] == 2 or occurrences[val] == 3:
                val_positions = []
                for position in blanks_in_boxes[box]:
                    if val in possible[position]:
                        val_positions.append(position)
                same_row, same_col = 0, 0
                for position in val_positions:
                    if val_positions[0][0] == position[0]:
                        same_row += 1
                    elif val_positions[0][1] == position[1]:
                        same_col += 1
                if same_row == len(val_positions):
                    for blank in blanks:
                        if blank not in blanks_in_boxes[box] and blank[0] == val_positions[0][0]:
                            try: possible[blank].remove(val)
                            except: pass
                if same_col == len(val_positions):
                    for blank in blanks:
                        if blank not in blanks_in_boxes[box] and blank[1] == val_positions[0][1]:
                            try: possible[blank].remove(val)
                            except: pass

            if occurrences[val] == 1:
                for position in blanks_in_boxes[box]:
                    if val in possible[position]:
                        sudoku[position[0]][position[1]] = val
                        del possible[position]
                        blanks_in_boxes[box].remove(position)
                        break

    solved = check(sudoku) # Checks if the sudoku is solved
    #Iterations are here for now because some sudoku are not solved by this algorithm

    if iteration == 50: # If even after 50 iterations the sudoku is not solved, stops the loop
        solved = True
        for b in blanks_in_boxes:
            print(f"{b}: {blanks_in_boxes[b]}")
            for p in blanks_in_boxes[b]:
                print(f"{p}: {possible[p]}")
    iteration += 1

for row in sudoku:
    print(row)
