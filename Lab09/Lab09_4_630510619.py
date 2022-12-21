#630510619
#nuttawat khamwangsawat
#section003
#Lab09_04

def series(n):
    if n == 0:
        return 0
    elif (n - 1) % 2 == 1 or n-1 == 0:
        return 2*series(n-1) + 1  
    else:
        return 2*series(n-1) - 1
def main():
    n = int(input())
    print(series(n))
   
if __name__=='__main__':
    main()