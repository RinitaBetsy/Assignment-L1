'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 
      
dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
dict3={'Salary':5500}
dict4={'Age':26}

print(Merge(dict1, dict2)) 
print("Merged dictionaries:\n",dict2)

dict2.update(dict3)
dict2.update(dict4)
dict2.update({'Grade':'B1'})

print("updated dictionary:\n",dict2)


print("keys:\n",dict2.keys())
print("values:\n",dict2.values())
del dict2['Age']
print(dict2)