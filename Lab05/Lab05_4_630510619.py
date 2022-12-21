#630510619
#nuttawat khamwangsawat
#section003
#Lab05_04
def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
    if l2 > l1 + w1 or t2 > t1 + h1 or l2 + w2 < l1 or t2 +h2 < t1 :
        return False
    else:
        return True

def main():
    l1,t1,w1,h1 = map(int,input().split())
    l2,t2,w2,h2 = map(int,input().split())
    print(is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2))

if __name__ == "__main__":
    main()
