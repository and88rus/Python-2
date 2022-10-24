def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




    s = input("N = ")
    p = []
    m = [i + 1 for i in range (int(s))]
    pr = 1
    for i in range(int(s)):
        pr *= m[i]
        p.append(pr)
    print(p)