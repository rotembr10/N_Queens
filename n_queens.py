#RotemBrooks


def legal(partial, i):
    n = len(partial)
    temp = [partial[j].index("Q") for j in range (n) if "Q" in partial[j]]
    m = len(temp)
    if temp == []:
        return True
    down = [j for j in temp if j == i]
    diag1 = [j for j in temp if j - temp.index(j) == i - m]
    diag2 = [j for j in temp if j + temp.index(j) == i + m]

    res = (down == diag1 == diag2 == [])
    return res


def queens(n):
    partial = []
    return queens_rec(n, partial)
def queens_rec(n, partial):
    if len(partial) == n:
        return 1
    else:
        cnt = 0
        for i in range (n):
            if legal(partial, i):
                temp = [["" for i in range(n)]]
                temp[0][i] = "Q"
                cnt += queens_rec(n, partial + temp)
        return cnt

    
def legal_dragons(board, row, col):
    
    if board[row][col] == 'D':
        return False

    a,b = row-1,col
    while a >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a = a-1 

    a,b = row-1,col-1
    while a >= 0 and b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a,b = a-1, b-1

    a,b = row, col-1
    while b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        b = b-1

    a,b = row+1,col-1
    while a < len(board) and b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a,b = a+1,b-1

    return True 
    
    
    
def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)

def queens_dragons_rec(remaining, row, col, board):
    counter = 0
    if remaining == 1 and row == col == len(board)-1 and legal_dragons(board, row, col):
        return 1
    if row == len(board)-1 == col:
        return 0
    if legal_dragons(board, row, col):
        if remaining == 1 :
            counter += 1
        else:
            board[row][col] = 'Q'
            if row < len(board)-1:
                counter += queens_dragons_rec(remaining-1, row+1, col, board)
            else:
                counter += queens_dragons_rec(remaining-1, 0, col+1, board)
            board[row][col] = ' '
    if row < len(board)-1:
        counter += queens_dragons_rec(remaining, row+1, col, board)
    else:
        counter += queens_dragons_rec(remaining, 0, col+1, board)
    return counter
    



# A function to print nested lists as matrices row by row
def print_mat(mat):
    n = len(mat)
    for i in range(n):
        print(mat[i])


def concat_hor(mat1, mat2):
    n=len(mat1)
    mat3 = [0 for i in range(n)]
    for i in range(n):
        mat3[i] = [*mat1[i],*mat2[i]]
    return mat3
            
  

def concat_vert(mat1, mat2):
    n = len(mat1)+len(mat2)
    mat3 = [0 for i in range(n)]
    
    for i in range (len(mat1)):
        mat3[i] = [*mat1[i]]
        
    for j in range (len(mat1),len(mat1)+len(mat2)):
        mat3[j] = [*mat2[j-len(mat1)]]
        
    return mat3


def inv(mat):
    n=len(mat)
    inv_mat=[0 for i in range (n)]
    
    for i in range(n):
        inv_mat[i] = [0 if num == 1 else 1 for num in mat[i]]
        
    return inv_mat


def had(n):
    if n==0:
        return [[0]]
    return [concat_vert(concat_hor(had(n-1),had(n-1)),concat_hor(had(n-1),inv(had(n-1))))][0]




def subset_sum_search(L,s):
    
    if L == [] and s ==0 :
        return []
    elif L == []:
        return None
    elif s == 0:
        return []
    
    else:
        if L[0] == s:
            return [L[0]]
        else:
            with_v = subset_sum_search(L[1:],(s - L[0])) 
            if with_v != None:
                return [L[0]] + with_v
            else:
                return subset_sum_search(L[1:],s)



def acc(f, v, lst):
    if lst == []:
        return v
    return acc(f,f(v,lst[0]),lst[1:])

########
# Tester
########

def test():
    contains = lambda L, R : all(R.count(r) <= L.count(r) for r in R)
    L = [1, 2, 4, 8, 16]

    R = subset_sum_search(L, 13)
    if R == None or not sum(R) == 13 or not contains(L,R):
        print("Error in subset_sum_search")

    R = subset_sum_search(L, 32)
    if not R == None:
        print("Error in subset_sum_search")

    L = [i for i in range(1, 10)]
    R = subset_sum_search(L, 7)
    if R == None or not sum(R) == 7 or not contains(L,R):
        print("Error in subset_sum_search")    
    
    if had(0) != [[0]]:
        print("Error in had")

    if had(2) != [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]:
        print("Error in had")

    n = 5        
    empty_board = [[' ' for i in range(5)] for j in range(5)]
    if queens_dragons(empty_board) != 10:
        print("Error in queens_dragons")
    
    if queens(5) != 10:
        print("Error in queens")
    board = [[' ', ' ', 'Q', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            [' ', 'Q ', 'D', 'Q', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            ['Q', ' ', 'D', ' ', ' ']]

    if legal_dragons(board, 2, 4) or not legal_dragons(board, 4, 4):
        print("Error in legal_dragons")
    
    board8 = [[' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
             ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    if legal(board8, 1) or not legal(board8, 3):
        print("Error in legal")

    def mysum(lst):
    	return acc((lambda x, y: x + y), 0, lst)
    
    lst = [i for i in range(1,25)]
    if mysum(lst) != sum(lst):
        print("Error in acc()")

        
