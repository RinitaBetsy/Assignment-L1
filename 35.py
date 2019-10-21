'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
tup_1=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print (tup_1)
tup_2=('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
print(tup_1+tup_2)
tup1=(3,9)
tup2=(5,7)
tup3=(8,2)
if(tup1>tup2)and(tup1>tup3):
    print(tup1)
elif(tup2>tup1)and(tup2>tup3):
    print(tup2)
else:
    print(tup3)
tup=list(tup_1)
print(tup)
tup.append('good')
print(tup)
tup.remove('sunday')
print(tup)
tup.clear()
print(tup)