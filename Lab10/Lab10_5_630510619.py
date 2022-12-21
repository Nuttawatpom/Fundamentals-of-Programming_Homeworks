#630510619
#nuttawat khamwangsawat
#section003
#Lab010_05

def three_digits_to_word(n):
    answer = ""
    unit1_9 = ["","one","two","three","four","five","six","seven","eight","nine",]#list 1 - 9
    unit10_19 = ["ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen"]#list 10 - 19
    unit20_90 = ["","","twenty","thirty", "forty","fifty","sixty", "seventy", "eighty", "ninety",""]#list 20 - 90
    x,y = divmod(n,100)
    if x == 0:
        y,z = divmod(n,10)
        if y == 0:
            answer = "".join(unit1_9[z])
        else:
            if y == 1:
                answer = "".join(unit10_19[n%10])
            else:
                if z != 0:
                    answer = "".join(unit20_90[y]) + "-" + "".join(unit1_9[z])
                else:
                    answer = "".join(unit20_90[y]) + "".join(unit1_9[z])
    else:
        answer = "".join(unit1_9[x]) + " hundred "
        n %= 100
        y,z = divmod(n,10)
        if y == 0:
            answer += "".join(unit1_9[z])
        else:
            if y == 1:
                answer += "".join(unit10_19[n%10])
            else:
                if z != 0:
                    answer += "".join(unit20_90[y]) + "-" + "".join(unit1_9[z])
                else:
                    answer += "".join(unit20_90[y]) + "".join(unit1_9[z])
    return answer
    
    
def num_to_word(num):
    if num == 0:
        return "zero"
    n = []
    k = ""
    while num > 0 or num < 0 :
        n.append(num%1000)
        num //= 1000
    n.reverse()

    lion = ["billion","million","thousand",""]
    z = 0

    if len(n) == 1:
        k += "".join(three_digits_to_word(n[0]))
    elif len(n) == 2:
        for i in n:
            if i != 0:
                k += "".join(three_digits_to_word(n[z]))
                k += " "
                k += "".join(lion[z+2])
                if n[1] != 0:
                    k += " "
                z += 1
    elif len(n) == 3:
        z = 3
        for i in n:
            if i != 0:
                k += "".join(three_digits_to_word(n[z-3]))
                k += " "
                k += "".join(lion[z-2])
                if n[z-(z-1)] != 0:
                    k += " "
                z += 1
    elif len(n) == 4:
        z = 0
        for i in n:
            if i != 0:
                k += "".join(three_digits_to_word(n[z]))
                k += " "
                k += "".join(lion[z])
                k += " "
                z += 1
        k = k[:-1]
    return k


def main():
    num = int(input())
    print(num_to_word(num))

if __name__ == "__main__":
    main()