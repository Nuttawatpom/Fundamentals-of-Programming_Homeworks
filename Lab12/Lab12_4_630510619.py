#630510619
#nuttawat khamwangsawat
#section003
#Lab12_04

def polynomial_addition(p1, p2):
    p1 = list_(p1)#represent p1 in funtion list_
    p2 = list_(p2)#represent p2 in funtion list_
    t = []#list collec value
    answer = []#answer list
    if p1 == []:#check p1 not []
        return p2
    elif p2 == []:#cheack p2 not []
        return p1
    for i in p1:
        for j in p2:
            if i[0] != j[0]:#check position 0 for p1 and p2
                a = False
            else:
                a = True
                break
        if a == False and i[1] != 0:#conditon answer
            answer.append(i)
    for i in p2:
        for j in p1:
            if i[0] != j[0]:#check position 0 for p2 and p1
                a = False
            else:
                a = True
                break
        if a == False and j[1] != 0:
            answer.append(i)
    for i in p1:
        for j in p2:
            if i[0] == j[0]:
                if i[1] + j[1] == 0:
                    continue
                t.append(i[0])
                t.append(i[1] + j[1])
        t = tuple(t)#change t for list to tuple
        if t != ():
            answer.append(t)
        t = []
    return sorted(answer, reverse = True)#answer

def list_(p):
    w = dict()
    t = []
    s = []
    for i in p:
        if i[0] not in w:
            w[i[0]] = i[1]
        else:
            w[i[0]] += i[1]
    for i in w:
        t.append(i)
        t.append(w[i])
        s.append(tuple(t))
        t = []
    return s

            
def main():
    p1 = [(2, 6), (1, 34), (0, -8)]
    p2 = [(2, -6), (0, 2), (1, 1)]
    print(polynomial_addition(p1,p2))

if __name__=='__main__':
    main()