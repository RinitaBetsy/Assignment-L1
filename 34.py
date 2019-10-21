'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from functools import reduce
  
def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 
List1=[23,14,62,47,86]
List2=[90,76,45,32,11]
List3=[3,4,87,12,32]

List1.sort()
max_L1=[List1[-1],List1[-2]]
print("Max elements in List1:",max_L1)
Avg_1=Average(max_L1)
print(Avg_1)

min_L1=[List1[0],List1[1]]
print("Min elements in List1:",min_L1)
Avg1=Average(min_L1)
print(Avg1)

List2.sort()
max_L2=[List2[-1],List2[-2]]
print("Max elements in List2:",max_L2)
Avg_2=Average(max_L2)
print(Avg_2)

min_L2=[List2[0],List2[1]]
print("Min elements in List2:",min_L2)
Avg2=Average(min_L2)
print(Avg2)



List3.sort()
max_L3=[List3[-1],List3[-2]]
print("Max elements in List3:",[List3[-1],List3[-2]])
Avg_3=Average(max_L3)
print(Avg_3)

min_L3=[List3[0],List3[1]]
print("Min elements in List3:",min_L3)
Avg3=Average(min_L3)
print(Avg3)
