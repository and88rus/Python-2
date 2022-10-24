def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(size1, L):
     print (" ")
     for i in range(int(size1)):
      elem = int(input((f'L[{i}] = ')))
      L.append(elem)




def creation_of_L1(size1, L, size2, L1):
 if (size2%2 == 1):
    for i in range(int(size1)-1, size2-2, -1):
        elem = L[i]
        L1.append(elem)
 if (size2%2 == 0):
    for i in range(int(size1)-1, size2-1, -1):
        elem = L[i]
        L1.append(elem)




def creation_of_L2(size2, L, L1, L2):
    for i in range(size2):
        elem = L1[i]
        L2.append(elem)
    for i in range (size2):
        L2[i] *= L[i]




def out_put_of_L2(size1, L2):
    print (" ")
    print (str(L2).strip('[]'))




L = []
L1 = []
L2 = []
size1 = int(input("Размер списка: "))
size2 = 0
if (size1%2 == 0): 
 size2 = size1 // 2
elif (size1%2 == 1):
    size2 = size1 // 2 + 1
creation_of_L(size1, L)
creation_of_L1(size1, L, size2, L1)
creation_of_L2(size2, L, L1, L2)
out_put_of_L2(size1, L2)
