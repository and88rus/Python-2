def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(L, n):
    print (" ")
    for i in range(int(n)):
     elem = int(input((f'L[{i}] = ')))
     L.append(elem)




def cout_of_L(L, L1, n):
    for i in range (int(n)):
        if (L.count(L[i]) == 1):
            L1.append(L[i])




L = []
L1 = []
n = int(input("Размер списка: "))  
creation_of_L(L, n)
print (" ")
print (L)
cout_of_L(L, L1, n)
print (" ")
print (L1)
