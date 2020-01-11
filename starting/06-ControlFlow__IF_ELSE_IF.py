# Ask for current temperature
temperature = input('What is the temperature? ')
#Convert temperature from string to float (number)
temperatureAsNumber = float(temperature)
#Print msg based on temperature - note colon ':', at end of IF, ELIF and ELSE lines; note indentation 
if temperatureAsNumber > 20:
    print('Wear shorts.')
elif temperatureAsNumber > 10: 
    print('Wear  pants.')
elif temperatureAsNumber > -10:
    print('Wear  warm pants.')
else:
    print('It is realy cold!')
print('The end.')