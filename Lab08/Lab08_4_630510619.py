#630510619
#nuttawat khamwangsawat
#section003
#Lab08_04

import string

def uniform(line):
    x = string.ascii_letters
    w = 0#collect lower letters
    t = 0#collect upper letters
    e = string.punctuation
    r = string.whitespace
    for i in line :
        if i in x and i not in e and i not in r :
            a = x.index(i)
            if a < 26 :#a-z 
                w += 1
            else:#A-Z 
                t += 1
    if w > t :
        return line.lower()#change lower all
    elif t > w :
        return line.upper()#change upper all
    elif w == t :
        a = x.index(line[0])
        if a < 26 :
            return line.lower()#change lower all
        else:
            return line.upper()#change upper all
        

def main():
    line = input()
    print(uniform(line))

if __name__ == '__main__':
    main()