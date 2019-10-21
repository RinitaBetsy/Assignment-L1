'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def bubblesort(arr):
    n=len(arr)
    for i in range (n):
        for j in range(0,n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j],arr[j+1]
    
arr=[23,76,8,5,2,1]
bubblesort(arr)
print("The sorted array:\n")
for i in range(len(arr)):
    print(arr[i],end=" ")