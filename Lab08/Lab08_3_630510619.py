#630510619
#nuttawat khamwangsawat
#section003
#Lab08_03

def patterned_message(message, pattern):
    w = message.replace(' ', '')

    while 1 <= len(pattern):
        for i in w:
            for j in pattern:
                
                if j == '*':
                    print(j.replace('*', i), end ='')#change * to i
                    pattern = pattern[1:]#cut * front
                    break

                elif j == '\n':
                    print()
                    pattern = pattern[1:]#cut * front

                elif j == ' ':
                    print(' ',end='')
                    pattern = pattern[1:]#cut * front
            

def main():
    message = input()
    pattern = input()
    patterned_message(message, pattern)

if __name__=='__main__':
    main()