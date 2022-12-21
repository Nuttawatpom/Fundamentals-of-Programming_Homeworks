#630510619
#nuttawat khamwangsawat
#section003
#Lab03_01
import math

def find_r_from_surface_area(surface_area):#faction find r_from_surface_area
    p = math.pi
    radius = (surface_area/4/p)**(1/2)#Equation find radius
    return radius

def sphere_volume(radius):#faction find sphere_volume
    p = math.pi
    volume = (4/3)*p*(radius**3)#Equation find volume
    return volume

def main():#faction find volume
    surface_area = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface_area)
    volume = sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))
main()