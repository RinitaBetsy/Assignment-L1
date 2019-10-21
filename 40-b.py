'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import timeit
from functools import reduce
code_to_test = """

List1_ele = ['Madurai','Thirunelveli','Trichy','Chennai','Mumbai']
List2_ele = ['Bengaluru','Delhi','Goa','Indore','Pune']
List3_ele = ['Cochin','Patna','Rameshwaram','Thiruchur','Coimbatore']

for word in List1_ele:
    print(word,":",len(word))
print(max(List1_ele))    

for ele in List2_ele:
    print(ele,":",len(ele))

for ele in List3_ele:
    print(ele,":",len(ele))
    """
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


