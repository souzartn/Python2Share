import random
import datetime
import os

selectedYear=1991
def ClearScreen():
    os.system('cls')
    return
def PrintMonthSample(selectedYear):
    speryear = input("How many {0} will you save each month?(only the number)".format(currency))
    peryear = int(speryear)
    year = input("What will be your first year of saving?")
    year2 = int(year)
    endyear = input("What will be your last year of saving?")
    endyear2 = int(endyear)
    month=1
    day=1
    money=0
    while year2<=endyear2:
        while month <=12:
            monthName=datetime.date(selectedYear, month, day).strftime('%B') 
            monthnamelength=len(monthName)
            money=money+peryear
            if monthnamelength<8:
                newmonth=monthName+"     "    
            else:
                newmonth=monthName
            print("{0}\t-\t{1}\t-\t{2} ".format(year2,  newmonth, money))
            month=month+1
        month=1
        year2=year2+1
    return money
 
# ----------- Main program -----------
ClearScreen()
currency = input("What currency will you bee using?(plural)")
money=PrintMonthSample(2019)
print("~~~~~~~~~After you finish saving, you will have {0} {1} in your savings.~~~~~~~~~".format(money, currency))