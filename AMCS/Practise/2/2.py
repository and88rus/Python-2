import random




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def creation_of_L(L,n,a,b):
    for i in range(int(n)):
        elem=random.random()*random.randint(a,b)
        L.append(elem)




def output_of_L(L):
    print (L)
    print (" ")




def sort_of_L_up(L,n): 
    t=0
    for j in range(int(n)-1):
        for i in range(int(n)-j-1):
            if L[i] > L[i+1]:
                t=L[i]
                L[i]=L[i+1]
                L[i+1]=t




def sort_of_L_down(L,n): 
    t=0
    for j in range(int(n)-1):
        for i in range(int(n)-j-1):
            if L[i] < L[i+1]:
                t=L[i]
                L[i]=L[i+1]
                L[i+1]=t                





L=[]



n = int(input("n = "))
print (" ")


a = float(input("a = "))
print (" ")


b = float(input("b = "))
print (" ")



creation_of_L(L,n,a,b)



output_of_L (L)




sort_of_L_up(L,n)




output_of_L (L)




sort_of_L_down(L,n)




output_of_L (L)