#630510619
#nuttawat khamwangsawat
#section003
#Lab07_02

def digit_count(x, base=10):
    w = 1
    while abs(x) // base != 0:
        x = abs(x) // base#find number to divide
        w += 1#collect value
    return w

def main():
    x = int(input())
    y = int(input())
    print(digit_count(x, y))

if __name__ == '__main__':
    main()