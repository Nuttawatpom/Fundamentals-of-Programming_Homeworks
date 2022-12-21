#630510619
#nuttawat khamwangsawat
#section003
#Lab07_03

def triangle(n):
    print("*")#start
    t = 1
    for _ in range(1, n-1):#loop find mid
        print("*" + t*"." + "*")
        t += 2
    print(n*"* ")#finish off
    
def main():
    n = int(input())
    print(triangle(n))

if __name__ == '__main__':
    main()