############################################################################
#This code tells you your message with each letter moved over two characters
############################################################################


message = input("What would you like to chipher?")
messagel=len(message) 
number=0
result=""

while number<messagel:
    letter=message[number]
    ln=ord(letter)
    ln=ln+2
    if ln>122:
        ln=ln-26
    else:
        ln=ln
    nl=chr(ln)
    number=number+1
    result=result + nl

print(result)