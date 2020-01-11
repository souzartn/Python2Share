# Ask for current temperature
temperature = input('What is the temperature? ')
#Convert temperature from string to float (number)
temperatureAsNumber = float(temperature)
#Print msg based on temperature - note colon ':' at end of IF and ELSE lines; note indentation 
if temperatureAsNumber > 18 and temperatureAsNumber<50:
    print('Wear shorts.')
else:
    print('Wear long pants.')
print('The End.')