def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(s, L):
   print (" ")
   for i in range(int(s)):
     elem = int(input((f'L[{i}] = ')))
     L.append(elem)




def output_of_L(s, L):
    print (" ")
    print (str(L).strip('[]'))




def sum_of_elem(s, L):
    sum = 0
    for i in range(int(s)): 
          if (i % 2 == 1):
            sum += L[i]
    print (" ")
    print ("Сумма элементов на нечетных позициях:")
    print (" ")
    print (sum)




L = []
s = int(input("Размер списка: "))
creation_of_L(s, L)
output_of_L (s, L)
sum_of_elem(s, L)