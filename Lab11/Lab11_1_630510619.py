#630510619
#nuttawat khamwangsawat
#section003
#Lab11_01

def matrix_mult(m1, m2):
    m = len(m1)#row m1
    n = len(m1[0])#column m1
    p = len(m2)#row m2
    q = len(m2[0])#column m2
    a = []#list bigger
    t = []#list collect value1
    u = []#list collect value2
    if n == p:#check condition matrix
        for i in range(m):#len row m1
            for k in range(q):#len column m2
                s = 0#reset value s
                for j in range(p):#len row m2
                    s += m1[i][j] * m2[j][k]#value s each row m1 with column m2
                t.append(s)#collect value t
            u = t[:]#copy value t
            a.append(u)#collect last list
            t = []#reset list t
        return a#answer
    else:
        return None

def main():
    m1 = [[1, 2, 3],[4, 5, 6]]
    m2 = [[7, 8],[9, 10],[11, 12]]
    print(matrix_mult(m1, m2))

if __name__=='__main__':
    main()