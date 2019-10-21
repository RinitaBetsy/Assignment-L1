'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def binarySearch(arr, l, f, x): 

	while f <= l: 

		mid = f + (l - f)//2; 
		
	
		if arr[mid] == x: 
			return mid 

		 
		elif arr[mid] < x: 
			f = mid + 1

	
		else: 
			l = mid - 1
	
	
	return -1

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print( "success" )
else: 
	print ( "not success" )

