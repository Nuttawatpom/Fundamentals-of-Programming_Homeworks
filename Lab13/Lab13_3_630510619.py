#630510619
#nuttawat khamwangsawat
#section003
#Lab13_03

import string

def word_count(text):
    s = []
    o = string.punctuation + string.whitespace
    g = text.lower()#change  all str be lower
    w = dict()#set cellec
    x = g.split('\n')#skipleave line
    for i in x:
        s.extend(i.split(' '))#Skip spece
    t = []
    for j in s:
        if j not in o:
            t.append(j)
    a = 0
    for k in t:
        s = k.strip(string.punctuation)#Skip spece
        t[a] = s
        a += 1
    for i in t:
        collec = 1 + w.get(i, 0)
        w[i] = collec
    return w

def main():
    text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
    print(word_count(text))

if __name__=='__main__':
    main()