#630510619
#nuttawat khamwangsawat
#section003
#Lab010_01

import string

def is_anagram(str1, str2):
    a = sorted(str1.lower())#Change upper to lower and Arrgange letter
    b = sorted(str2.lower())#Change upper to lower and Arrgange letter
    s1 = ''#collec string.ascii_letters
    s2 = ''#collec string.ascii_letters
    for i in a:
        if i in string.ascii_letters:#check list str1
            s1 += i
    for i in b:
        if i in string.ascii_letters:#check list str2
            s2 += i
    if s1 == s2:#check value s1 and value s2
        return True
    else:
        return False
    
def main():
    str1 = input()
    str2 = input()
    print(is_anagram(str1, str2))
   
if __name__=='__main__':
    main()