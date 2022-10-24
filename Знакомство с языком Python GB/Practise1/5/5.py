import math
def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



    
    def distance_between_2points(x1,x2,y1,y2):
        d=(math.pow((x2-x1),2)+math.pow((y2-y1),2))**0.5
        return d



        
    print ("Введите координаты точки A")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    print ("Введите координаты точки B")
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    print (distance_between_2points(x1,x2,y1,y2))