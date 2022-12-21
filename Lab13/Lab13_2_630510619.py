#630510619
#nuttawat khamwangsawat
#section003
#Lab13_02

from functools import reduce

def power_set(set_a):
    w = lambda set_a: reduce(lambda P, x: P + [subset | {x} for subset in P], set_a, [set()])
    return w(set_a)
    
def main():
    set_a = {'a', 'b', 'c'}
    print(power_set(set_a))

if __name__=='__main__':
    main()