#630510619
#nuttawat khamwangsawat
#section003
#Lab12_01

import string

def sort_date(list_x):
    w = '/'
    index = 0
    for a in list_x:#separate string in list
        list_x[index] = a.split(w)#separate string for /
        index += 1#change position
    for a in list_x:
        for b in range(0, len(a)):
            a[b] = int(a[b])#change string to int
    for a in list_x:
        a[0], a[2] = a[2], a[0]#switch day and year
    list_x.sort()#sort int in list_x
    for a in list_x:
        for b in range(0, len(a)):
            a[b] = str(a[b])#change int to string
    for a in list_x:
        a[0], a[2] = a[2], a[0]#switch year and day
        continue
    for a in range(0, len(list_x)):
        list_x[a] = w.join(list_x[a])#add / in list_x

def main():
    list_x =["11/1/2100","5/12/1999","19/1/2003","11/9/2001"]
    sort_date(list_x)
    print("---")
    print(list_x)

if __name__=='__main__':
    main()