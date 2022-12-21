#630510619
#nuttawat khamwangsawat
#section003
#Lab06_01
def int_power(x, y):#loop exponent
    n = 1
    while y > 0:#positive exponent
        n = n * x
        y = y - 1
    while y < 0:#nagative exponent
        n = n / x
        y = y + 1
    return n


def main():
    x = float(input())
    y = int(input())
    print(int_power(x, y))

if __name__ == '__main__':
    main()