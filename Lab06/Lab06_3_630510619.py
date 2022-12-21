#630510619
#nuttawat khamwangsawat
#section003
#Lab06_03

import math#call math
def factorize(x):
    if is_prime(x):
        print ("%d is prime"%(x))
    else:
        i = 2
        print("%d is "%x,end ="")
        while i <= (math.sqrt(x)):
            if x % i == 0:
                x = x//i
                print(i,"*",end =" ")
            else:
                if i > 2:
                    i = i + 2
                else:
                    i = i + 1
        print(x)

def is_prime(x):
    t = 0
    for i in range(1, x+1):
        if x % i == 0:
            t = t + 1
            if t > 2:
                break
    if t > 2:
        return False
    else:
        return True

def main():
    x = int(input())
    factorize(x)
   
if __name__ == '__main__':
    main()