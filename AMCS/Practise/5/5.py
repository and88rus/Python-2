import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def roots(a,b,c):
    if ((math.pow (b,2)-4*a*c)>0):
       x1=(-b+math.sqrt(pow (b,2)-4*a*c))/2*a
       x2=(-b-math.sqrt(pow (b,2)-4*a*c))/2*a
       return print("x1  = ",x1," ","x2  = ",x2)




    elif ((math.pow (b,2)-4*a*c)==0): 
         x=(-1)*b/2*a
         return print ("x0  = ",x)




    elif (((math.pow (b,2))-4*a*c)<0):
        return ("действительных корней нет")

 



a = int(input("a = "))
print (" ") 




b = int(input("b = "))
print (" ") 




c = int(input("c = "))
print (" ") 




(roots(a,b,c))