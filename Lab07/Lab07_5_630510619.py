#630510619
#nuttawat khamwangsawat
#section003
#Lab07_05

def rotate(num, pos):
    a = 0
    w = 0
    y = digit(num)-1
    if pos > 0:
        for i in range(1, pos+1):
            w = num % 10
            a = num // 10
            s = w * (10**y)
            num = s + a
        return num
    else:
        pos = abs(pos)#change value for pos
        for i in range(1, pos+1):
            w = num % 10**y
            s = w  * 10
            x = num - w
            a = x // 10**y
            num = s + a
        return num
        
def digit(num):#number of digits
    e = 0
    x = num
    while x > 0:
        x = x // 10
        e += 1
    return e

def main():
    num = int(input())
    pos = int(input())
    print(rotate(num, pos))

if __name__ == '__main__':
    main()