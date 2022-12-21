#630510619
#nuttawat khamwangsawat
#section003
#Lab06_02
def float_to_bin(x):#funtion Decimal page number
    w = 0
    n = 0
    a = abs(int(x))
    while a > 0:
        r = a % 2#r=remainder
        s = a // 2
        a = s
        n = n + (r*(10)**w)
        w = w + 1#Exponent
    
    if x > 0:
        return n + number_to_bin(x)
    else:
        return (n*(-1)) + number_to_bin(x)

def number_to_bin(x):#funtion Decimal after number
    b = x - int(x)
    q = 0
    t = 0
    for i in range(1, 7):
        y = b * 2
        q = int(y)
        t = t + (q*(10)**(-i))
        b = y - q
    return t

def main():
    x = float(input())
    print("%.6f"%(float_to_bin(x)))

if __name__ == '__main__':
    main()