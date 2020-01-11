#Here we define "x" global variable and assign a value to it
x=10
y=200
print('the value of x global variable is {0}'.format(x)) 

#Here define function  "MyFunction", it takes no paraments
def MyFunction():
    global y # this is the same global variable "y" 
    x=2 #This is a local variable, unrelated to "x" global variable
    print('the value of x local variable (inside MyFunction) is {0}'.format(x))

    y=300
    print('the value of y global variable (inside MyFunction) is {0}'.format(y))

print('starting program...')
# Call function  "MyFunction" passing no parameters
MyFunction()
print('the value of x global variable before the end of the program is {0}'.format(x)) 
print('the value of y global variable before the end of the program is {0}'.format(y)) 
print('The end.')