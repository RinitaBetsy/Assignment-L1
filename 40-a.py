'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import datetime
import time
from datetime import timedelta  

curr_time=datetime.datetime.now()
end_time=curr_time + timedelta(seconds=60)
print("start time is "+ str(curr_time))
print("end time is "+ str(end_time))
while curr_time <= end_time :
    curr_time=datetime.datetime.now()
    print(curr_time)
    time.sleep(5)




