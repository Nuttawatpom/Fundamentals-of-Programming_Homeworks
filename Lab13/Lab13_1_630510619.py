#630510619
#nuttawat khamwangsawat
#section003
#Lab13_01

def count_segment(list_a):
    a = 0 
    b = 0 
    c = 0
    e = 0

    for i in list_a:
        x = i[0]
        y = i[1]
        z = i[2]
        r = ((x**2)+(y**2))**1/2
        if x > 0 and y > 0:
            a += 1
            if r < z:
                c += 1
            if x - z < 0:
                b += 1
            if y - z < 0:
                e += 1
        elif x < 0 and y > 0:
            b += 1
            if r < z:
                e += 1
            if abs(x) - z < 0:
                a += 1
            if y - z < 0:
                c += 1
        elif x < 0 and y < 0:
            c += 1
            if r < z:
                a += 1
            if abs(x) - z < 0:
                e  += 1
            if abs(y) - z < 0:
                b += 1
        elif x > 0 and y < 0:
            e += 1
            if r < z:
                b += 1
            if x - z < 0:
                c += 1
            if abs(y) - z < 0:
                a += 1
        elif x == 0 and y > 0:
            a += 1
            b += 1
            if y - z < 0:
                c += 1
                e += 1
        elif x == 0 and y < 0:
            c += 1
            e += 1
            if abs(y) - z < 0:
                a += 1
                b += 1
        elif y == 0 and x > 0:
            a += 1
            e += 1
            if abs(x) - z < 0:
                b += 1
                c += 1
        elif y == 0 and x < 0:
            b += 1
            c += 1
            if abs(x) - z < 0:
                a += 1
                e += 1
        elif x == 0 and y == 0 and z > 0:
            a += 1
            b += 1
            c += 1 
            e += 1
    return (a, b, c, e)
        
def main():
    list_a = [(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3), (7.2, -2.8, 1.2)] 
    print(count_segment(list_a))

if __name__=='__main__':
    main()