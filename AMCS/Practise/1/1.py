def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def quantity_of_diviers_of_n(n):
  L=[]
  for i in range (1,int(n)+1,+1):
    if (n%i==0):
      L.append(i)
  return (len(L))




n = int(input("n = "))
print (" ")
if (quantity_of_diviers_of_n(n)==2):
    print (f'{n} - простое число')
elif (quantity_of_diviers_of_n(n)>2):
    print (f'{n} - составное число')
elif (quantity_of_diviers_of_n(n)==1):
    print (f'{n} - ни простое и не составное число')