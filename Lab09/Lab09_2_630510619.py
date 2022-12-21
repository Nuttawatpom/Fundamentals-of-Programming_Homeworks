#630510619
#nuttawat khamwangsawat
#section003
#Lab09_02

def n_base_to_10(n,num):
    if num == 0:
        return 0
    else:
        return n * (n_base_to_10(n,num//10)) + (num%10)
def main():
    n = int(input())
    num = int(input())
    print(n_base_to_10(n,num))
   
if __name__=='__main__':
    main()