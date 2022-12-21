#630510619
#nuttawat khamwangsawat
#section003
#Lab11_04
def sum_nested_list(list_a):
    s = list_a[:]#copy list
    for i in s:
        if isinstance(i, list):#check i with list
            while isinstance(i, list):
                s.extend(i)#change i for list and add 
                break
            continue
    for i in range(len(s)):
        if isinstance(s[i], list):#check position s[i] with list
            s[i] = 0#change list = 0
    return sum(s)#sum total value

def main():
    list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]
    print(sum_nested_list(list_a))

if __name__=='__main__':
    main()