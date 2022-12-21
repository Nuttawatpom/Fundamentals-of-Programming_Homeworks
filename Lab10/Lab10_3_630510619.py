#630510619
#nuttawat khamwangsawat
#section003
#Lab10_03

def nondest_rotate_list(list_a, n):
    w = list_a[:]#back up list_a in w
    a = list_a[:]#back up list_a in a
    if n > 0:
        t = n % len(w)#check value n
        w = w[t*(-1):]#select position list
        a = a[:t*(-1)]#select position list
        s = w + a#value answer list
        return w
    else:
        n = abs(n)
        t = n % len(w)#check value n
        w = w[:t]#select position list
        a = a[t:]#select position list
        s = a + w#value answer list
        return s

def main():
    list_a = [1, 2, 3, 4]
    n = int(input())
    print(nondest_rotate_list(list_a, n))

if __name__=='__main__':
    main()