#630510619
#nuttawat khamwangsawat
#section003
#Lab13_04

def square_matrix(list_x):
    row = len(list_x)#value row of list_x
    w = 0#collec value len col
    plus_0 = 0#collec value of the most row or col 
    for i in range(row):
        col = len(list_x[i])
        if col > w: 
            w = col
    if row > w:#check len row and col
        plus_0 += row
    else:
        plus_0 += w
    t = []
    for i in range(plus_0 - len(list_x)):#loop for col martix
        for j in range(plus_0):
            t.append(0)
        s = t[:]#collec list t
        list_x.append(s)#add zero in list_x by condition loop for col
        t = []#reset list t
    for i in list_x:#loop for row martix
        for j in range(plus_0 - len(i)):
            i.append(0)

def main():
    list_x = [[1, 2],[1, 2, 3],[1, 2],[1, 2],[1]]
    print(square_matrix(list_x))
if __name__=='__main__':
    main()