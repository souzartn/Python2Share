#Here define function  "print_max"  that takes two paraments: a and b
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

print('starting program...')
# Call function  "print_max" passing values 3 and 4 to parameters "a" and "b" respectively 
print_max(3, 4)

# Call function  "print_max" AGAIN passing values 7 and 7 to parameters "a" and "b" respectively 
print_max(7, 7)

# Call function  "print_max" AGAIN passing values 20 and 10 to parameters "a" and "b" respectively 
print_max(20, 10)
print('The end.')