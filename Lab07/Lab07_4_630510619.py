#630510619
#nuttawat khamwangsawat
#section003
#Lab07_04

def life_path(x):
    n = x
    t = 0
    w = 0
    g = 0
    while n > 0:
        a = n % 10
        t += a#collect value1
        n = n // 10
    if t >= 10:
        while t > 0:
            s = t % 10
            w += s#collect value2
            t = t // 10
        if w >= 10:
            while w > 0:
                k = w % 10
                g += k#collect value3
                w = w // 10
            return g#value 3
        else:
            return w#value 2
    else:
        return t#value 1
        

def main():
    x = int(input())
    print(life_path(x))

if __name__ == '__main__':
    main()