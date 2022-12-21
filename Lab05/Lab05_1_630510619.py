#630510619
#nuttawat khamwangsawat
#section003
#Lab05_01
def intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6):
    d = (((x2-x1)**2 + (y2-y1)**2)**0.5)

    if d > r1 and d > r2 :
        if abs(d - (r1+r2)) <= epsilon :
            result = 0
        elif d < r1 + r2 :
            result = 1
        else:
            result = -1
    else:
        if r1 > r2 :
            r_max = r1
            r_min = r2
        else:
            r_max = r2
            r_min = r1
        if abs(r_max - r_min - d) <= epsilon :
            result = 0
        elif r_max - r_min - d < 0 :
            result = 1
        else:
            result = -1   
    return result

def main():
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    print(intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6))

if __name__ == '__main__':
    main()