#630510619
#nuttawat khamwangsawat
#section003
#Lab04_04
def calculate_p2p_evolve_exp(p, c):#funtion find exp form pokemon
    x = c//12#find Pidgeotto
    if p > x:
        a = x
        c = c - (a*12)
        p = p - a
        c = a + c 
    else:
        a = p
        p = 0
        c = c - (a*12)
        c = a + c
    if p > 0:#Pidgey left
        if p + c > 12:
            a = a + 1
            p = p - 1 - (12-c)
            c = c - 12 + p
    if c >= 1:#candy must have 1
        a = a + p//12
    return a *500#answer
        
    
def main():
    p = int(input())
    c = int(input())
    
    print(calculate_p2p_evolve_exp(p, c))#print funtion

if __name__ == '__main__' :
    main()