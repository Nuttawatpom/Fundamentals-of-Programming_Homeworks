#630510619
#nuttawat khamwangsawat
#section003
#Lab03_04
def kth_digit(number,k):
    return (abs(number)//(10**k))%10#Calculation formula

def main():
    number = int(input())#set number
    k = int(input())#find digit
    a = kth_digit(number,k)#use Function
    print(a)#answer
    
if __name__ == '__main__' :
    main()
