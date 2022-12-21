#630510619
#nuttawat khamwangsawat
#section003
#Lab05_03
def count_down_to_songkran(d, m, y):
    fe1 = feb1(y)
    fe2 = feb2(y)
    if d > 0: 
        if m == 1:
            return (75+fe1)-d
        elif m == 2:
            return (fe1+44)-d
        elif m == 3:
            return 44-d
        elif m == 4:
            if d <= 13:
                return 13-d
            else:
                return (30-d)+245+(75+fe2)
        elif m == 5:
            return (31-d)+214+(75+fe2)
        elif m == 6:
            return (30-d)+184+(75+fe2)
        elif m == 7:
            return (31-d)+153+(75+fe2)
        elif m == 8:
            return (31-d)+122+(75+fe2)
        elif m == 9:
            return (30-d)+92+(75+fe2)
        elif m == 10:
            return (31-d)+61+(75+fe2)
        elif m == 11:
            return (30-d)+31+(75+fe2)
        elif m == 12:
            return (31-d)+(75+fe2)

def feb1(y):
    if y / 4 == int(y / 4) :
        if y % 100 == 0 :
            if y % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28    
            
def feb2(y):
    if (y+1) / 4 == int((y+1) / 4) :
        if (y+1) % 100 == 0 :
            if (y+1) % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

def main():
    d,m,y = map(int,input().split())
    print(count_down_to_songkran(d, m, y))    
            
if __name__== '__main__':
    main()