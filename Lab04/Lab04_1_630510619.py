#630510619
#nuttawat khamwangsawat
#section003
#Lab04_01
def love6(first, second):#function if else
    if first == 6:#First condition
        return True
    elif second == 6:#second condition
        return True
    elif first + second == 6:#Third condition
        return True
    elif abs(first - second) == 6:#Fourth condition
        return True
    else :#condition to False
        return False

def main():#use function
    first = int(input())#set number for first
    second = int(input())#set number for second
    print(love6(first, second))#answer

if __name__ == '__main__' :
    main()