#630510619
#nuttawat khamwangsawat
#section003
#Lab02_03
print("First Equation")
m1 = float(input("Input m1: "))#set slop1
b1 = float(input("Input b1: "))#set b1
print("Second Equation")
m2 = float(input("Input m2: "))#set slop2
b2 = float(input("Input b2: "))#set b2
x = (b1-b2)/(m2-m1) #process Evaluate x
y = (m1*x) + b1 #process Evaluate y
print("The point of intersection is at x = %.2f and y = %.2f" %(x,y))#intersection point