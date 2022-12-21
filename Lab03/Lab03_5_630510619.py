#630510619
#nuttawat khamwangsawat
#section003
#Lab03_05
def set_kth_digit(number, k,value):
    x = (value-kth_digit(number,k))*(10**k)#Change value
    return x + number

def kth_digit(number,k):
    return (abs(number)//(10**k))%10#Calculation formula

def main():#use function
    number = int(input())#set number
    k = int(input())#find digit
    value = int(input())#set value
    a = set_kth_digit(number,k,value)#use function
    print(a)#answer
    
if __name__ == '__main__' :
    main()