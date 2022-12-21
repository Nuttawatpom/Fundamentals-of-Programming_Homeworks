#630510619
#nuttawat khamwangsawat
#section003
#Lab08_05

def decode(code_table, text):
    a = len(code_table)
    s = code_table
    w = text.replace('\n', ' \n ')#add space bar
    d = w.split(" ")   
    for i in d:
        if i == '\n':
            print()
        elif i.isdigit():
            for j in s:
                if s.find(j) == int(i):
                    print(j, end='')
                elif int(i) >= a:
                    print('_',end='')
                    break
        elif i =='':
            continue
        else:
            print('_',end='')
                 