"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
TodayMonth = month_name[datetime.today().month]
TodayDate = datetime.today().day

Name = input("Hello, what is your name? ")
BirthMonth = input("Hi "+Name+", what was the name of the month you were born in? ")
BirthYear = input("And what year were you born in, "+Name+"? ")
BirthDay = int(input("And the day? "))

if BirthMonth == "October" and BirthDay == 31:
    print("You were born on Halloween!")
    
if BirthMonth == TodayMonth and BirthDay == TodayDate:
    print("Happy Birthday!")