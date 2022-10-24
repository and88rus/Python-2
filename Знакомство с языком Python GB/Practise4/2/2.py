def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def dividers_of_n(L1,n):
  for i in range (1, int(n)):
    if (n%i == 0):
     L1.append(i)




def quantity_of_dividers_of_n(n):
  L=[]
  for i in range (1, int(n)+1):
    if (n%i == 0):
     L.append(i)
  return len(L)




def quanity_of_prime_dividers_of_n(L2,L1,n):
 while (n>1):
  for i in range (0,len(L1)):
   if ((n%L1[i]==0) & (L1[i]!=1) & (quantity_of_dividers_of_n(L1[i])==2)):
    n//=L1[i]
    L2.append (L1[i])




L1=[]
L2=[]
n = int(input("N = "))
dividers_of_n(L1,n)
quanity_of_prime_dividers_of_n(L2,L1,n)
print (" ")
print ('простые множители числа',n,'следующие:')
print (" ")
print (L2)