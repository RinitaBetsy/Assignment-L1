'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def check_palin(s): 
   rev = ''.join(reversed(s)) 
   if (s == rev): 
        return True
   return False
  
s = "mam"
ans = check_palin(s) 
  
if (ans): 
    print("The given string is palindrome") 
else: 
    print("The given string is not a palindrome") 