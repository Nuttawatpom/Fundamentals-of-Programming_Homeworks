#630510619
#nuttawat khamwangsawat
#section003
#Lab11_02

import copy

def remove_row_col(list_a, row, col):
    w = copy.deepcopy(list_a)#copy list_a
    m = len(list_a)#row list_a
    n = len(list_a[0])#column list_a
    if row < m and row >= -m:
        del w[row]#delete row(w)
    if col < n and col >= -n:
        for i in range(len(w)):
            del w[i][col]#delete col (w)
    return w
        
def main():

    list_a = [[2, 3, 4, 5],[8, 7, 6, 5],[0, 1, 2, 3]]
    row = 1
    col = 2
    print(remove_row_col(list_a, row, col))

if __name__=='__main__':
    main()