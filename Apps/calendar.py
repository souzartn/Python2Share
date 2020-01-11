##########################################################################
# Util: Consider person that put aside CDN 20/month for 20 years on his/her savings.
#       Create a program that will Print total amount that person will have saved each month   
#      e.g.
#           Year    -   Month   - Amount (CDN) 
#           2019    -   January  -   20
#           2019    -   February -   40
#           2019    -   March    -   60
# Uses:  while, for,  if,  elif, print, etc
##########################################################################
import random
import datetime
import os

def ClearScreen():
    os.system('cls')
    return
def CalenderMoneySavings(selectedYear):
    month=1
    day=1
    money=20
    year=2019
    while year<=2039:
        
        while month <=12:
            monthName=datetime.date(selectedYear, month, day).strftime('%B') 
            monthnamelength=len(monthName)
            if monthnamelength<8:
                newmonth=monthName+"     "    
            else:
                newmonth=monthName
            print("{0}\t-\t{1}\t-\t{2} ".format(year,  newmonth, money))
            month=month+1
            money=money+20
        month=1
        year=year+1
    return money-20

## ----------- Main program -----------
ClearScreen()
money=CalenderMoneySavings(2019)
print("After 20 years you will have ", money," money")