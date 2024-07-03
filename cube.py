def volume_cube(a):
    return (a*a*a)
    
def volume_cuboid(l , h ,w ):
    return (l*h*w)
    
def volume_sphere(r):
    return ((4/3)*3.142*(r * r * r) )
    
def Find_volume():
    print( "1 . is for VOlume Of Cube " )
    print( "2 . is for VOlume Of Cuboid " )
    print( "3 . is for VOlume Of Sphere " )

    option=int(input("Enter the option from (1,2 ,3) = "))
 
    if option == 1:
       a=int(input("Enter the side of cube = "))
       volume_of_cube= volume_cube(a) 
       print(f"The volume of cube is = {volume_of_cube}")


    elif option == 2:
        l=int(input("Enter the length of cuboid = "))
        h=int(input("Enter the height of cuboid = "))
        w=int(input("Enter the width of cuboid = "))
        volume_of_cuboid= volume_cuboid(l,h,w)
        print(f"The volume of cuboid is = {volume_of_cuboid}")
    else:
       r=int(input("Enter the radius of sphere = "))
       volume_of_sphere=volume_sphere(r)
       print(f"The volume of sphere is = {volume_of_sphere}")
               

Find_volume()