#630510619
#nuttawat khamwangsawat
#section003
#Lab03_02
def reverse_digits(x):#faction reverse_digits
    a = x//1000#find Unit
    b = ((x//100)%10)*10#find Tens
    c = ((x//10)%10)*100#find Hundreds
    d = (x%10)*1000#find Thousands
    z = d+c+b+a
    return z
    
def main():#function
    x = int(input())#set Number for kerbord
    y = reverse_digits(x)
    print(y)
    
if __name__ == '__main__' :
    main() 