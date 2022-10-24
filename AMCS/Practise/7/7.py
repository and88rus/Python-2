import math 




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()





def f(x):
    return math.sqrt(x)*math.sin(x)




def df(x,e):
 return (f((x+e))-f(x))/e




x = int(input("x0 = "))
print (" ")




e = int(input("e = "))
print (" ")




print (f' f^({x}) = {df(x,e)} при e = {e}')