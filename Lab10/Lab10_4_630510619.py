#630510619
#nuttawat khamwangsawat
#section003
#Lab09_04

def dest_rotate_list(list_a, n):
    t = n % len(list_a)#find round
    if t == 0:#full round
        return list_a#answer
    else:
        if n > 0:
            for i in range(n):
                w = list_a.pop(-1)#delete last list
                list_a.insert(0, w)#answer
        else:
            n = abs(n)#change Negative to Aective
            for i in range(n):
                w = list_a.pop(0)#delete frist list
                list_a.append(w)#answer

def main():
    list_a = [1, 2, 3, 4]
    n = -1
    dest_rotate_list(list_a, n)
    print(list_a)

if __name__=='__main__':
    main()