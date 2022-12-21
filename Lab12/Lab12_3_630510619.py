#630510619
#nuttawat khamwangsawat
#section003
#Lab12_03

def coprime_factor(a, b):
    a = prime_factor(a)
    b = prime_factor(b)
    t = []
    for i in a:#Pull numbers one by one in a
        if i in b:#compare i in b
            t.append(i)#cellec numbers of i in b
            del b[b.index(i)]#delete nsed numbers
    return t

def prime_factor(n):
    w = []
    while n % 2 == 0:#loop of n = 2
        w.append(2)
        n /= 2
    e = 3
    while e <= (n**0.5)+1:#loop of n > 2
        while n % e == 0:
            w.append(int(e))
            n = n / e
        e += 2
    if n > 2:
        w.append(int(n))
    return w
            
def main():
    n = 34
    a = 180
    b = 48
    print(coprime_factor(a, b))

if __name__=='__main__':
    main()