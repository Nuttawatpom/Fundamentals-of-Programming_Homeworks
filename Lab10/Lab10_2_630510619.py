#630510619
#nuttawat khamwangsawat
#section003
#Lab010_02

def classify(list_x):
    list_a = []#collec int
    list_b = []#collec float
    list_c = []#collec str
    for i in list_x:
        if isinstance(i, int):#check list_x
            list_a.append(i)
        elif isinstance(i, float):#check list_x
            list_b.append(i)
        elif isinstance(i, str):#check list_x
            list_c.append(i)
    return list_a, list_b, list_c

    
def main():
    list_x = [10, 'hello', 23.5, 4]
    print(classify(list_x))
   
if __name__=='__main__':
    main()