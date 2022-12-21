#630510619
#nuttawat khamwangsawat
#section003
#Lab08_01

def square_frame(n, sep=' '):
    w = []
    a = (n**2)-((n-2)**2)
    for i in range(1, a+1):
        if i <= 9:
            i = str(i)
            w.append('0'+i)
        else:
            w.append(i)
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j == 1:#แถวบน
                if k == n:
                    print(w[k-1],end = '')
                else:
                    print(w[k-1],end = sep)
            elif j == n:#แถวล่างสุด
                if k == n:
                    print(w[a-k-(n-2)],end = '')
                else:
                    print(w[a-k-(n-2)],end = sep)
            else:#แถวกลาง
                if k == 1:
                    print(w[-j+1],end = sep)
                elif k == n:
                    print(w[k+j-2],end='')
                else:
                    print(sep + sep, end = sep)
        print() 
