def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



    
    x = input(" x = ")
    y = input(" y = ")
    if (((int(x))>0 and ((int(y))>0))):
     print ("I четверть")
    elif (((int(x))<0 and ((int(y))>0))): 
     print ("II четверть")
    elif (((int(x))<0 and ((int(y))<0))): 
     print ("III четверть")
    elif (((int(x))>0 and ((int(y))<0))): 
     print ("IV четверть")
    elif (((int(x))==0) and (((int(y))>0) or ((int(y))<0))): 
     print ("ось Y")
    elif (((int(y))==0) and (((int(x))>0) or ((int(x))<0))): 
     print (" ось X")
    elif (((int(y))==0) and (((int(x))==0))): 
     print ("четверть неопределена, расположение на пересечении оси X и Y")