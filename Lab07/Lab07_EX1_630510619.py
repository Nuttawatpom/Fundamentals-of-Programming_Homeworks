#630510619
#nuttawat khamwangsawat
#section003
#Lab07_E1

def xmas_tree(n):
    tree = "\n"
    s1 = n + 2 
    a = 1 
    t = a 
    s = n + 1
    k = s #space bar
    b = n + 3
    tree += s*' '+'   |' + "\n" 
    tree += s*' '+' --*--' + "\n"
    tree += s1*' '+' /|\\ ' + "\n"
    tree += s1*' '+'/* *\\ ' + "\n"
    for i in range (1,n+1):
        for i in range (1,4):
            tree = tree + (s*' '+'/*'+' '+a*'* '+'*\\' + "\n")
            a += 1
            s -= 1
        t += 1
        a = t
        k -= 1
        s = k
    tree += b*' '+'|||' + "\n"
    tree += b*'_'+'|||'+b*'_'
    return tree
    

def main():
    n = int(input())
    print(xmas_tree(n))


if __name__ == '__main__' :
    main()    