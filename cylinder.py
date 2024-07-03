def cube_vol(a):
   
    return a*a*a

def cuboid_vol(l , w ,h):
    return l*h*w

def cylinder_vol(r , h):        
    return 3.142*(r*r)*h

choice=input("Enter your choice to find volume of : (cylinder , cube , cuboid ) = ")
if choice == "cube":
    a=int(input("Enter side of cube in cm = " ))
    cube=cube_vol(a)
    print ("The volume of cube is = ",cube ,"cm ^3" )

elif choice== "cuboid":
    l=int(input("Enter the length in cm = " ))
    h=int(input("Enter the height in cm = "  ))
    w=int(input("Enter the width in cm = " ))
    cuboid=cuboid_vol(l, h , w)  
    print ("The volume of cuboid = " ,cuboid , "cm^3")  

elif choice == "cylinder":
    r=int(input ("Enter thr radius in cm = "))
    h=int(input("Enter the height in cm = "))
    cylinder=cylinder_vol(r,h)
    print ("The volume of cylinder : ", cylinder ," cm^3")

else:
    print("Invalid")