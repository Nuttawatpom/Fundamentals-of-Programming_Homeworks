#630510619
#nuttawat khamwangsawat
#section003
#Lab08_02

import string

def is_palindrome(x, b):
    a = 0
    u = 0
    while x > 0:
        t = x % b
        a += t * (10**u)#change digits
        u += 1#collect number
        x = x // b
    w = str(a)#change a 
    l = (len(w)+1) // 2
    for i in range (0, l):
        if w[i] != w[-(i+1)]:#compare digits
            return False
    return True

def main():
    x, b = map(int,input().split())
    print(is_palindrome(x, b))

if __name__ == '__main__':
    main()