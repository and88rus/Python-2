def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def factorial_of_n(n):
     res=1
     for i in range (1,n+1,+1):
         res*=i
     return res




n = int(input("n = "))
print (" ") 
print (f"{n}! = {factorial_of_n(n)}")