from decimal import Decimal
import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L1(s, L1):
   print (" ")
   for i in range(int(s)):
     elem = float(input((f'L[{i}] = ')))
     L1.append(elem)




def output_of_L1(s, L1):
    print (" ")
    print (str(L1).strip('[]'))




def creation_of_L2(s, L1, L2):
    for i in range (int(s)):
        elem = float(Decimal(str(L1[i])) - int(float(str(L1[i]))))
        L2.append(elem)




def min_of_L2(s, L2):
    min = L2[0]
    for i in range (int(s)):
     if ((L2[i] < min) & (L2[i] != 0.0)):
        min = L2[i]
    return (min)




def max_of_L2(s, L2):
    max = L2[0]
    for i in range (int(s)):
     if (L2[i] > max):
        max = L2[i]
    return (max)




L1 = []
L2 = []
s = int(input("Размер списка: "))
creation_of_L1(s, L1)
output_of_L1 (s, L1) 
creation_of_L2(s, L1, L2)
print (" ")
print (abs(max_of_L2(s, L2) - min_of_L2(s, L2)))