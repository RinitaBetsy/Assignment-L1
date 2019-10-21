'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def vow_check(string,vowels):
    string=string.casefold()
    count = {}.fromkeys(vowels, 0) 
    
    for character in string :
        if character in count: 
            count[ character] += 1 
            return count
def vow_count(string,vowels):   
    
    final = [each for each in string if each in vowels] 
    return(len(final))
    

vowels = 'aeiou'
string = "Python is case sensitive"
print (vow_check(string, vowels)) 
print ("Total vowels:",vow_count(string, vowels)) 
