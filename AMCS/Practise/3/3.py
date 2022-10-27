def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def last_number_of_n(n):
    return n%10




def last_2_numbers_of_n(n):
  return n%100




def finish(n):
  if (last_2_numbers_of_n(n)==11 or last_2_numbers_of_n(n)==12 or last_2_numbers_of_n(n)==13 or last_2_numbers_of_n(n)==14):
    return " "
  elif (last_number_of_n(n)==1):
    return "а"
  elif (last_number_of_n(n)==2 or last_number_of_n(n)==3 or last_number_of_n(n)==4):
    return "ы"
  elif (last_number_of_n(n)==0 or last_number_of_n(n)==5 or last_number_of_n(n)==6 or last_number_of_n(n)==7 or last_number_of_n(n)==8 or last_number_of_n(n)==9): 
    return " "




n = int(input("n = "))




print (" ")




print (f'{n} коров{finish(n)}')