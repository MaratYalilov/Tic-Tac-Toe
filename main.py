import random

N=None
a=[N,N,N]
b=[N,N,N]
c=[N,N,N]

table = [a,b,c]

is_play = True
is_first = True
user = ''
i = 0
comp = 0
human = 1

def print_table(a_row, b_row, c_row):
    a0 = a_row[0]; a1 = a_row[1]; a2 = a_row[2]
    b0 = b_row[0]; b1 = b_row[1]; b2 = b_row[2]
    c0 = c_row[0]; c1 = c_row[1]; c2 = c_row[2]
    if a0 == N: a0 = ' '
    if a1 == N: a1 = ' '
    if a2 == N: a2 = ' '
    if b0 == N: b0 = ' '
    if b1 == N: b1 = ' '
    if b2 == N: b2 = ' '
    if c0 == N: c0 = ' '
    if c1 == N: c1 = ' '
    if c2 == N: c2 = ' '
    if a0 == 1: a0 = 'X'
    if a1 == 1: a1 = 'X'
    if a2 == 1: a2 = 'X'
    if b0 == 1: b0 = 'X'
    if b1 == 1: b1 = 'X'
    if b2 == 1: b2 = 'X'
    if c0 == 1: c0 = 'X'
    if c1 == 1: c1 = 'X'
    if c2 == 1: c2 = 'X'
    print(f"     0   1   2   ")
    print(f'a  | {a0} | {a1} | {a2}')
    print(f" ----------------")
    print(f'b  | {b0} | {b1} | {b2}')
    print(f" ----------------")
    print(f'c  | {c0} | {c1} | {c2}')
    print(f" ----------------")


def is_win():
    row_1 = a; row_2 = b; row_3 = c

    col_0 = [a[0], b[0], c[0]]
    col_1 = [a[1], b[1], c[1]]
    col_2 = [a[2], b[2], c[2]]

    dig_1 = [a[0], b[1], c[2]]
    dig_2 = [a[2], b[1], c[0]]

    if not N in a: row_1 = sum(a)
    if not N in b: row_2 = sum(b)
    if not N in c: row_3 = sum(c)
    if not N in col_0: col_0 = sum(col_0)
    if not N in col_1: col_1 = sum(col_1)
    if not N in col_2: col_2 = sum(col_2)
    if not N in dig_1: dig_1 = sum(dig_1)
    if not N in dig_2: dig_2 = sum(dig_2)


    list_matrix = [row_1, row_2, row_3, col_0, col_1, col_2, dig_1, dig_2]
    #print(list_matrix)
    global is_play
    if 0 in list_matrix:
        #is_play = False
        return 0 #'Комп выиграл 0'
    elif 3 in list_matrix:
        #is_play = False
        return 1 #'Человек ты выиграл  1'

    # if i == 9:
    #     #is_play = False
    #     return 9 #'Победила дружба'

def is_draw(act_table):
    return all(cell != N for row in act_table for cell in row)


def check_table(row_col, a_rows, b_rows, c_rows):
    row_col_list = list(row_col) # введённые юзером координаты ['a', '1']
    if len(row_col_list) != 2:
        print('Введите 2 знака')
        return False

    row = row_col_list[0]
    if not row in ['a','b','c'] :
        print('Строка может быть только a,b,c')
        return False

    col = row_col_list[1]
    if col not in ['0','1','2']:
        print('Колонка может быть только 1, 2, 3')
        return False

    col = int(row_col_list[1])
    bol_a = row == 'a' and a_rows[col] != N
    bol_b = row == 'b' and b_rows[col] != N
    bol_c = row == 'c' and c_rows[col] != N
    if bol_a or bol_b or bol_c:
        print(f'Уже есть значение в строке "{row}" столбце  "{col}"')
        return False

    return True



def change_table(act_user, row_col, a_rows, b_rows, c_rows):
    if act_user == 'comp':
        mark = 0
    else:
        mark = 1
    row_col_list = list(row_col)
    row = row_col_list[0]
    col = int(row_col_list[1])
    if row == 'a':
        a_rows[col] = mark
    if row == 'b':
        b_rows[col] = mark
    if row == 'c':
        c_rows[col] = mark


def find_empty():
    list_empty=[]
    indexes = ['a', 'b', 'c']
    row_count = 0
    for row in [a,b,c]:
        col_count = 0
        row_index = indexes[row_count]
        for item in row:
            if item == N:
                list_empty.append(str(row_index)+ str(col_count))
            col_count +=1
        row_count +=1
    return list_empty # ['a0', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']


def minimax(act_table, is_maximizing):
    if is_win() == 0:
        return 1 #print('Комп выиграл 0')
    elif is_win() == 1:
        return -1 #print('Человек ты выиграл  1')
    elif is_draw(act_table):
        return 0 #('Победила дружба')

    if is_maximizing:
        best_score = -10
        for row_i in range(3):
            for col_i in range(3):
                if table[row_i][col_i] == N:
                    act_table[row_i][col_i] = comp
                    score = minimax(act_table, False)
                    act_table[row_i][col_i] = N
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 10
        for row_i in range(3):
            for col_i in range(3):
                if act_table[row_i][col_i] == N:
                    act_table[row_i][col_i] = human
                    score = minimax(act_table, True)
                    act_table[row_i][col_i] = N
                    best_score = min(score, best_score)
        return best_score

def move():
    best_move = ()
    best_score = -10
    indexes = ['a', 'b', 'c']
    for row_i in range(3):
        for col_i in range(3):
            if table[row_i][col_i] == N:
                table[row_i][col_i] = comp
                score = minimax(table, False)
                table[row_i][col_i] = N
                if score > best_score:
                    best_score = score
                    row_index = indexes[row_i]
                    best_move = str(row_index)+str(col_i)

    # Вариант игры со случайными ходами компа
    #return random.choice(find_empty())
    # Вариант игры с AI
    print(best_move)
    return best_move


while is_play:
    input_user = ''
    if is_first:
        print_table(a, b, c)
        is_first = False

    if i%2 == 0:
        user = 'human'
        input_user = input(f"Давай ходи {user}! Type like 'a1': ")
    else:
        user = 'comp'
        input_user = move()
        print(input_user)

    if check_table(input_user, a, b, c):
        change_table(user, input_user, a, b, c)
        i += 1

    print_table(a, b, c)
    print(find_empty())

    if is_win() == 0:
        is_play = False
        print('Комп выиграл')
    elif is_win() == 1:
        is_play = False
        print('Человек ты выиграл')
    elif is_draw(table):
        is_play = False
        print('Победила дружба')








