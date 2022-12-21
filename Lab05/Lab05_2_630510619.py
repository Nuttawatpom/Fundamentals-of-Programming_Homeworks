#630510619
#nuttawat khamwangsawat
#section003
#Lab05_02
def is_p_triple(a, b, c):#funtion triple
    if c**2 + a**2 == b**2:
        return True
    if c**2 + b**2 == a**2:
        return True
    if c**2 == a**2 + b**2:
        return True
    else:
        return False

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(is_p_triple(a, b, c))

if __name__ == '__main__':#use funtion
    main()
