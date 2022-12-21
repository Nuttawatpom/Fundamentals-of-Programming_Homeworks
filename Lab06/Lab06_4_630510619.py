#630510619
#nuttawat khamwangsawat
#section003
#Lab06_04

def Total_Max_students(x):
    max_ = 0
    runner_up = 0
    point = 0
    for _ in range(x):#loop find max , runner up and  average
        score = float(input())
        if score > max_:
            runner_up = max_#Change value runner_up
            max_ = score#Change value max
        elif max_ > score > runner_up:
            runner_up = score#find value runner_up
        point = point + score#Total point students
    average = abs(point/x)#find average
    print("---")
    print("Max score is: %.2f"%(max_))
    if max_ == average:
        print("Runner up is: None")
    else:
        print("Runner up is: %.2f"%(runner_up))
    print("Average is: %.2f"%(average))
    
def main():
    x = int(input("Total students: "))
    print("Enter score:")
    Total_Max_students(x)#use funntion

    
if __name__ == '__main__':#use funtion main
    main()