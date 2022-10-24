import math




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()



    
    s = input("n = ")
    m = [math.pow((1 + 1/(i + 1)),(i + 1)) for i in range (int(s))]
    sum = 0
    for i in range(int(s)):
        sum += m[i]
    print (round(sum, 3))