#630510619
#nuttawat khamwangsawat
#section003
#Lab03_03
def square(x):#function find sqare volume
    square = x * x
    return square
    
def triangle(x):#function find triangle volume
    triangle = (1/2)*((x/3)**2)
    return triangle

def octagon_area():#function find octadon volume
    x = float(input(""))
    a = square(x)
    b = triangle(x)*4
    result = a-b
    print("%.6f" % result, type(result))
octagon_area()