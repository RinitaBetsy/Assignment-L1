'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from functools import reduce


def Sorting(lst): 
    lst.sort(key=len) 
    return lst     

   
List1_ele = ['Madurai','Thirunelveli','Trichy','Chennai','Mumbai']
List2_ele = ['Bengaluru','Delhi','Goa','Indore','Pune']
List3_ele = ['Cochin','Patna','Rameshwaram','Thiruchur','Coimbatore']
l1=[]

for word in List1_ele:
    print(word,":",len(word))
for ele in List2_ele:
    print(ele,":",len(ele))
for ele in List3_ele:
    print(ele,":",len(ele))
        

Sorting(List1_ele)
print("Max:",List1_ele[-1])
print("Min:",List1_ele[0])
l1.append(List1_ele[-1])
l1.append(List1_ele[0])


Sorting(List2_ele)
print("Max:",List2_ele[-1])
print("Min:",List2_ele[0])
l1.append(List2_ele[-1])
l1.append(List2_ele[-0])


Sorting(List1_ele)
print("Max:",List3_ele[-1])
print("Min:",List3_ele[0])
l1.append(List3_ele[-1])
l1.append(List3_ele[-0])


Sorting(l1)
print("city with biggest length:",l1[-1])
print("city with smallest length:",l1[0])


(List1_ele.pop(0))
(List1_ele.pop(-1))
(List2_ele.pop(0))
(List2_ele.pop(-1))
(List3_ele.pop(0))
(List3_ele.pop(-1))
print(List1_ele)
print(List2_ele)
print(List3_ele)


       

