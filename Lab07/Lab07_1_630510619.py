#630510619
#nuttawat khamwangsawat
#section003
#Lab07_01

def sum_prime_in_range(x, y):
    w = 0
    if x != y :#check value x and y
        for a in range(x, y+1):
            for b in range(2, a):
                if a % b == 0:#check prime
                    break
            else:
                w += a#collect value
        return w
    elif x == y :#value x = y
        for b in range(2, x):
            if x % b == 0 :
                return 0
        else:
            return x


def main():
    x = int(input())
    y = int(input())
    print(sum_prime_in_range(x, y))

if __name__ == '__main__':
    main()