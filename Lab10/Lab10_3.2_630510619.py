#630510619
#nuttawat khamwangsawat
#section003
#Lab09_01

def nondest_rotate_list(list_a, n):
    w = list_a[:]
    s = '' 
    for i in range(1, len(w)+1):
        s += str(i)
    k = int(s)
    if n > 0:
        n = n % 10
        for i in range(1, n+1):
            a = k % 10
            k = k // 10
            t = a * (10**(len(w)-1))
            k = k + t
    else:
        n = abs(n)
        n = n % 10
        for i in range(1, n+1):
            a = k // (10**(len(str(k))-1))
            k = (k % (10**(len(str(k))-1)))*10
            k = k + a
    u = str(k)
    r = []
    for i in range(len(u)):
        r.append(int(u[i]))
    return r


def main():
    list_a = [1, 2, 3, 4]
    n = int(input())
    print(nondest_rotate_list(list_a, n))

if __name__=='__main__':
    main()