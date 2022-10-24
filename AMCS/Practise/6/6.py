def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def cout_of_words(str):
  k=0 
  x=' '
  string=list(str)
  for i in range (1,len(string)-1):
   if (string[len(string)-1]!=x):
    string.append(' ')
  for i in range (1,len(string)):
    if ((string[i]==x) & (string[i-1]!=x)):
     k=k+1
  return (k)




print ("Введите строку:")




print (" ")




str = input()




print (" ")




print (f'Кол-во введенных слов - {cout_of_words(str)}.')