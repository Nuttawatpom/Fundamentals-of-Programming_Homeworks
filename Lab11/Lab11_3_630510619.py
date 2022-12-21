#630510619
#nuttawat khamwangsawat
#section003
#Lab11_03

def is_magic_square(board):
    m = len(board)#row
    n = len(board[0])#col
    w = 0#collec value
    k = []#list collec value row
    e = []#list collec value col
    a = []#list collec value col
    q = []#list collec value 1 col
    l = []#list collec value board
    v = []#list collec value 1 to n**2
    for i in range(m):
        for j in range(n):
            w += board[i][j]
            l.append(w)
            w = 0
    for i in range(1,(n**2)+1):
        v.append(i)
        
    if n * m == n**2 and sorted(l) == v:
        for i in board:
            w += sum(i)
            k.append(w)
            w = 0
        for i in range(m):
            for j in range(n):
                t = board[j][i]
                e.append(t)
            r = e[:]
            a.append(r)
            e = []
        for i in a:
            w += sum(i)
            q.append(w)
            w = 0
        p = 0#collec value
        h = []#list collec value Diagonal
        for i in range(n):
            w += board[i][p]
            p += 1
            h.append(w)
            w = 0
        h = sum(h)#tatal Diagonal
        p = n-1
        y = []#list collec value Diagonal
        for i in range(n):
            w += board[i][p]
            p -= 1
            y.append(w)
            w = 0
        y = sum(y)#tatal Diagonal
        c = 0#collec value
        d = 0#collec value
        for i in k:#check value k
            if i == h and i == y:
                c += 1
        for i in q:#check value q
            if i == h and i == y:
                d += 1
        if h == y and k == q and c == n and d == n and c == d:
            return True
        else:
            return False
    else:
        return False

def main():
    board = [[7, 12, 14, 1],
 [2, 13, 11, 8],
 [9, 6, 4, 15],
 [16, 3, 5, 10]]
    print(is_magic_square(board))

if __name__=='__main__':
    main()