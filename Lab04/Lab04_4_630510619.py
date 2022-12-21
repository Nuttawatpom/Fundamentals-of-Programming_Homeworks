#630510619
#nuttawat khamwangsawat
#section003
#Lab04_04
def round_to_int(x):
    if x >= 0:#x=0 or x=positive number
        if (x - int(x)) >= 0.5:#decimal more than 0.5
            return int(x) + 1
        else:
            return int(x)
    if x <= 0:#x=0 or x=negative number
        if abs(x - int(x)) >= 0.5:#decimal more than 0.5
            return -(abs (int(x)) + 1)
        else:
            return int(x)

def main():
    x = float(input())
    print(round_to_int(x))
    round_to_int(x)#use funtion round_to_int

if __name__ == '__main__' :#use funtion main
    main()