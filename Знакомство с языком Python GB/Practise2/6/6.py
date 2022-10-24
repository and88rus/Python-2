def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def inn(str, substr):
     k = 0
     for i in range(len(str) - len(substr) + 1):
        if str[i:i + len(substr)] == substr:
            k += 1
     print (f'Количество вхождений "{substr}" в "{str}": ' ,k)




str = input("Основная строка: ")
print (" ")
substr = input("Подстрока по отношению к основной: ")
print (" ")
inn(str,substr)
