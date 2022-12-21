#630510619
#nuttawat khamwangsawat
#section003
#Lab04_05
def nearest_odd(x):
    if x > int(x): #Positive decimal condition 
        if int(x)/2 == int(x/2) :#Positive number
            return int(x)+1#answer positive number
        else:
            return int(x)#Nwgative number
    if x < 0:  #Negative decimal and integer condition
        if x == int(x):
            if x/2 == int(x/2) :#Positive number
                return int(x)+1#answer positive number
            else:
                return int(x)
        if -(int(x)/2) == -(int(x/2)):#Positive number
            return int(x)-1#answer positive number
        else:
            return int(x)
    if x > 0:    #Positive integer condition
        if x == int(x):
            if x/2 == int(x/2) :#Positive number
                return int(x)+1#answer positive number
            else:
                return int(x)
    if x == 0: #condition x=0
        return int(x+1)#answer x=0
    else:
        return int(x+1)#answer x=0

def main():
    x = float(input())#set number on keybord
    nearest_odd(x)#use funtion nearest_odd
    print(nearest_odd(x))

if __name__ == '__main__' :#use funtion main
    main()