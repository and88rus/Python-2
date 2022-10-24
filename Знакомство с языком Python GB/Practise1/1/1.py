def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



    
    d = input("Введите день недели:")
    if (((int(d))==1) or ((int(d))==2) or ((int(d))==3) or ((int(d))==4) or ((int(d))==5)):
     print ("это будний день")
    elif (((int(d))==6) or (int(d)==7)): 
     print ("это выходной день")

