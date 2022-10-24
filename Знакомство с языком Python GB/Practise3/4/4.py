def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def translation(n):
    b = ''
    while n > 0:
     b = str(n % 2) + b
     n = n // 2
    return b




n = int(input("n = "))
print (" ")
print (f'{n}[10] = {translation(n)}[2]')