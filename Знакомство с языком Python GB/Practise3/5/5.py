import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def fibonacci(n):
    if (n >= 2):
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif (n == 1):
        return 1
    elif (n == 0):
        return 0
    elif (n < 0):
        return int(math.pow(-1,(-1 * n + 1)) * fibonacci(-1 * n))




def creating_of_fibonacci_list(n, L):
    for i in range (-int(n), int(n) + 1, +1):
     elem = fibonacci(i)
     L.append(elem)




def output_of_L(L):
   print (" ")
   print (str(L).strip('[]')) 




L = []
n = int(input("k = "))
creating_of_fibonacci_list(n, L)
output_of_L(L)
