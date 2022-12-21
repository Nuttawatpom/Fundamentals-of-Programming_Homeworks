#630510619
#nuttawat khamwangsawat
#section003
#Lab09_01

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
def main():
    x = int(input())
    y = int(input())
    print(gcd(x, y))
   
if __name__=='__main__':
    main()