#630510619
#nuttawat khamwangsawat
#section003
#Lab06_05

def longest_digit_run(n):
    k = 1
    m = 0#the largest collector
    while n > 0:
        x = n % 10#main unit
        y = (n // 10) % 10#ten digit
        if x == y:
            k = k + 1
        else:
            k = 1 
        n = n // 10
        if k > m:
            m = k
        else:
            m = m        
    return m
    

def main():
    n = int(input())
    print(longest_digit_run(n))

if __name__ == '__main__':
    main()