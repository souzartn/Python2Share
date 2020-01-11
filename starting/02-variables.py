# number: integer
age = 20
# number: float (decimals e.g. 1.23)
price = 100.13
#String: can be defined with single or double quotes
msg = ' Hello world!'
msg2 = "Hello world!" 
#Hello world with a variable 
print(msg) 

#Concatenation (combining strings) 
firstName = 'albert' 
lastName = 'einstein' 
fullName = firstName + ' ' + lastName 
print(fullName)
#Print with format method
print('My name is {0}, I am {1} years old'.format(fullName,age))

#Boolean variables can be True or False. 
myTrue = True
myFalse = False
print (myTrue)
# the "not" keyword can  be used to inverse a boolean value
print(not myFalse)

# read data from the keyboard in python 
userAge = input('How old are you? ')
print('Your are {0} years old'.format(userAge))


