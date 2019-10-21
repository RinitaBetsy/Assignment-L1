'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''


dict1={1:"cat",2:"rabbit",3:"kitten"}
dict2={1:"lion",2:"tiger",3:"bear"}
dict3={1:"deer",2:"dog",3:"elephant"}

dict1[4]="monkey"
dict2[4]="parrot"
length=int(0)
final_val=''
maindict=[]
maindict.append(dict1)
maindict.append(dict2)
maindict.append(dict3)

for dict_each in maindict:
    for j in dict_each:
        temp_length=len(dict_each[j])
        if temp_length > length:
            length=temp_length
            final_val=dict_each[j]
print("String which has Greatest length " + final_val)
print("Dict1:\n",dict1,len(dict1),type(dict1))
res1=str(dict1)
print(res1,type(res1))


print("\nDict2:\n",dict2,len(dict2),type(dict2)) 
res2=str(dict2)
print(res2,type(res2))

print("\nDict3:\n",dict3,len(dict3),type(dict3))
res3=str(dict3)
print(res3,type(res3))
print(res1+res2+res3)






