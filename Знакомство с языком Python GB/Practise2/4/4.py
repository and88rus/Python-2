def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




    s = input("N = ")
    print (" ")
    m = [i for i in range (-int(s), int(s) + 1)]
    print(m)
    print (" ")
    a = int(input("a = "))
    print (" ")
    b = int(input("b = "))
    print (" ")
    print ("m[",a,"]"," * ","m[",b,"] = ", m[a] * m[b])