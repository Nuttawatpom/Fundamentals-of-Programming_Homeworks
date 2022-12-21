#630510619
#nuttawat khamwangsawat
#section003
#Lab04_02
def my_max_mid_min(a, b, c):
    if a > b :#compare a and b
        max_ = a
        min_ = b 
    else:#compare b and a
        max_ = b
        min_ = a
    if c > max_ :#compare c and max_
        max_ = c
    if c < min_ :#compare c and min_
        min_ = c
    mid_ =  (a + b + c) - (max_) - (min_)#find value mid
       
    print("max = %d"%max_)#answer max
    print("mid = %d"%mid_)#answer mid
    print("min = %d"%min_)#answer min 
def main():
    a = int(input())#set a on keybord
    b = int(input())#set b on keybord
    c = int(input())#set c on keybord
    my_max_mid_min(a, b, c)

if __name__ == '__main__' :
    main()