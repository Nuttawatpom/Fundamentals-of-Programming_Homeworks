#630510619
#nuttawat khamwangsawat
#section003
#Lab09_03

def is_prime(n):
    return c_is_prime(n, 2)
    
def c_is_prime(n, x):
    if int(n**0.5) + 1 == x:
        return True
    else:
        if n % x == 0:
            return False
        return c_is_prime(n, x + 1)
 
def main():
    n = int(input())
    print(is_prime(n))
   
if __name__=='__main__':
    main()