#630510619
#nuttawat khamwangsawat
#section003
#Lab09_05
import math
def reverse_num(num):
    if num  < 10:
        return num
    else:
        k = 10**math.floor(math.log(num,10))
        return k*(num%10) + reverse_num(num//10)

def main():
    num = int(input())
    print(reverse_num(num))
   
if __name__=='__main__':
    main()