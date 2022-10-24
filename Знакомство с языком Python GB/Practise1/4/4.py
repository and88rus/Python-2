def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



    
    c = input("Введите четверть плоскости:")
    if (int(c)==1):
     print ("x>0","y>0")
    elif (int(c)==2): 
     print ("x<0","y>0")
    elif (int(c)==3): 
     print ("x<0","y<0")
    elif (int(c)==4): 
     print ("x>0","y<0")