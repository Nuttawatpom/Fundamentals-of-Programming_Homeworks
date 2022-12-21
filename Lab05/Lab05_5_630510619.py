#630510619
#nuttawat khamwangsawat
#section003
#Lab05_05
def zodiac_element(year):
    x = year
    if x % 12 == 0 :
        y = "Monkey"
    if x % 12 == 1 :
        y = "Rooster"
    if x % 12 == 2 :
        y = "Dog"
    if x % 12 == 3 :
        y = "Pig"
    if x % 12 == 4 :
        y = "Rat"
    if x % 12 == 5 :
        y = "Ox"
    if x % 12 == 6 :
        y = "Tiger"
    if x % 12 == 7 :
        y = "Rabbit"
    if x % 12 == 8 :
        y = "Dragon"
    if x % 12 == 9 :
        y = "Snake"
    if x % 12 == 10 :
        y = "Horse"
    if x % 12 == 11 :
        y = "Goat"
    return element(x) + " " + y
def element(x):
    if x % 10 == 0 or x % 10 == 1:
        return "Metal"
    if x % 10 == 2 or x % 10 == 3:
        return "Water"
    if x % 10 == 4 or x % 10 == 5:
        return "Wood"
    if x % 10 == 6 or x % 10 == 7:
        return "Fire"
    if x % 10 == 8 or x % 10 == 9:
        return "Earth"
def main():
    x = int(input())
    print(zodiac_element(year))
    
if __name__ == '__main__':
    main()