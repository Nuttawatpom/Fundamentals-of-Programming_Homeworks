#630510619
#nuttawat khamwangsawat
#section003
#Lab07_E2

def pyramid_stairs(n):
    w = 22
    s = 2
    a = 1
    t = 0
    k = 10

    if n >= 1 :
        for _ in range (1,n):
            w += 10
            s += 5
            a += 5
        for i in range (1,n+1):
            if i == 1:
                print(s * " " + "o" + 2 * " " + 12 * "*" + 2 * " " + "o")
                print(a * " " + "/" + "|" + "\\" + " " + "*" + 10 * " " + "*" + " " + "/" + "|" + "\\")
                print(a * " " + "/" + " " + "\\" + " " + "*" + 10 * " " + "*" + " " + "/" + " " + "\\")
            elif i > 1 :
                print(s * " " + "o" + 2 * " " + 6 * "*" + t * " " + 6 * "*" + 2 * " " + "o")
                print(a * " " + "/" + "|" + "\\" + " " + "*" + k * " " + "*" + " " + "/" + "|" + "\\")
                print(a * " " + "/" + " " + "\\" + " " + "*" + k * " " + "*" + " " + "/" + " " + "\\")
            t += 10
            k += 10
            s -= 5
            a -= 5
    if n > 0:
        print(w * "*")
    

def main():
    n = int(input())
    (pyramid_stairs(n))
if __name__ == '__main__' :
    main()