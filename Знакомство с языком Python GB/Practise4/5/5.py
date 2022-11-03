import random




def print_hi():
    print()
if __name__ == '__main__':
    print_hi()




def monom(monoms,k): 
   a=0
   b=0
   unL=[]
   if (i==0):
    b = k
    a = random.randint(0,100)
   else:
    a = random.randint(0,100)
    b = random.randint(0,k)
   unL.append (a)
   unL.append (b)
   monoms.append(unL)




def sum_of_monoms(monoms,couficients_of_monoms,degrees_of_monoms_for_sum_of_monoms,degrees_of_monoms):
  for i in range (0,len(monoms)):
    if monoms[i][1] in degrees_of_monoms_for_sum_of_monoms:
      continue
    c=monoms[i][0]
    d=monoms[i][1]
    for j in range (i+1,len(monoms)):
        if ((monoms[i][1]==monoms[j][1])):
            c+=monoms[j][0]
            degrees_of_monoms_for_sum_of_monoms.append(monoms[j][1])
    couficients_of_monoms.append(c) 
    degrees_of_monoms.append(d)




def forming_of_polynom(a, b,polynom):
    unL=[]
    for i in range (0, 1):
       unL.append (a)
       unL.append (b)
    polynom.append(unL)




def sort_of_polynom_by_low_index (polynom): 
   t=0
   for j in range(0,len(polynom)-1):
      for i in range(0,len(polynom)-j-1):
         if (polynom[i][1] < polynom[i+1][1]):
                t=polynom[i]
                polynom[i]=polynom[i+1]
                polynom[i+1]=t





def voz(polynom):
  if ((polynom[i][0]==0) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==0) and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]>1) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]>1) and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]==0) and (polynom[i][1])>1):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])>1):
     return "^"
  elif ((polynom[i][0]>1) and (polynom[i][1])>1):
     return "^"
 

  

def deg(polynom):
  if ((polynom[i][0]==0) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==0)and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]==1)and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]>1) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]>1)and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]==0) and (polynom[i][1])>1):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])>1):
     return str(polynom[i][1])
  elif ((polynom[i][0]>1) and (polynom[i][1])>1):
     return str(polynom[i][1])
 
  

  
def x(polynom):
  if ((polynom[i][0]==0) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==0) and (polynom[i][1])==1):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])==1):
     return "x"
  elif ((polynom[i][0]>1) and (polynom[i][1])==0):
     return ""
  elif ((polynom[i][0]>1)and (polynom[i][1])==1):
     return "x"
  elif ((polynom[i][0]==0) and (polynom[i][1])>1):
     return ""
  elif ((polynom[i][0]==1) and (polynom[i][1])>1):
     return "x"
  elif ((polynom[i][0]>1) and (polynom[i][1])>1):
     return "x"
 


 
def couf(polynom):
  if ((polynom[i][0]==0) and (polynom[i][1])==0):
     return ''
  elif ((polynom[i][0]==0) and (polynom[i][1])==1):
     return ''
  elif ((polynom[i][0]==1) and (polynom[i][1])==0):
     return "1"
  elif ((polynom[i][0]==1) and (polynom[i][1])==1):
     return ''
  elif ((polynom[i][0]>1) and (polynom[i][1])==0):
     return str(polynom[i][0])
  elif ((polynom[i][0]>1)and (polynom[i][1])==1):
     return str(polynom[i][0])
  elif ((polynom[i][0]==0) and (polynom[i][1]>1)):
     return ''
  elif ((polynom[i][0]==1) and (polynom[i][1])>1):
     return ''
  elif ((polynom[i][0]>1) and (polynom[i][1])>1):
     return str(polynom[i][0])




def plus(polynom):
    if ((i!=len(polynom)-1) and (polynom[i][0]!=0)):
        return (" + ")
    elif ((i==len(polynom)-2) and (polynom[len(polynom)-1][0]==0)):
      return ('')
    else: 
        return ('')




monoms=[]




couficients_of_monoms=[]




degrees_of_monoms=[]




degrees_of_monoms_for_sum_of_monoms=[]




polynom=[]




k = random.randint(0,10)




for i in range (0, int(k)+1):
 monom(monoms,k)




sum_of_monoms(monoms,couficients_of_monoms,degrees_of_monoms_for_sum_of_monoms,degrees_of_monoms)




for i in range (0, len(degrees_of_monoms)):
    forming_of_polynom(couficients_of_monoms[i],degrees_of_monoms[i],polynom)




sort_of_polynom_by_low_index(polynom)




for i in range (0, len(polynom)):
    polynom[i][0]=random.randint(0,100)




print(" ")




for i in range (0,len(polynom)):
    if (polynom[i][0]):
     print (f'{couf(polynom)}{x(polynom)}{voz(polynom)}{deg(polynom)}{plus(polynom)}',end = " ")
    if (i==len(polynom)-1):
         print ("= 0")
print()




data = open('for 4 of 4.txt','w')




for i in range (0,len(polynom)):
  if ((couf(polynom)!='') or (polynom[i][0]!=0)):
     data.write(couf(polynom))
  data.write(x(polynom))
  data.write(voz(polynom))
  data.write(deg(polynom))
  data.write(plus(polynom))
  if (i==len(polynom)-1):
         data.write (" = 0")




data.close()




exit()