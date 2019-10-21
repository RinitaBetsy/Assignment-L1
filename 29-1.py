'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
str= "rinita betsy"
print("capitalize : ",str.capitalize())
print(str.center(40 ,'$' ))
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'used'
print ("String.count('used', 10, 40) : ", str.count(sub,10,40))
enc=str.encode('ascii','strict')
print("encoded str:",enc)
dec=enc.decode('ascii','strict')
print("decoded str:",dec)