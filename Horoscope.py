import os
from datetime import date
def program():
    Year = input("year of birth: ")
    Month = input("month of birth: ")
    Day = input("Day of birth: ")
    Date_Of_Birth = (Day + "/" + Month + "/" + Year)
    print('Your Date of Birth is ' + Date_Of_Birth)
    d = date.today()
    y = d.year
    os.system("cls")
    age = y - int(Year)
    print('Your age is ' + str(age))



    if ((int(Month)==12 and int(Day)>=22)or(int(Month)==1 and int(Day)<=19)):
        zodiac_sign = ("Capricorn")
    elif((int(Month)==1 and int(Day)>=20)or(int(Month)==2 and int(Day)<=18)):
        zodiac_sign = ("Aquarius")
    elif ((int(Month)==2 and int(Day)<=19)or(int(Month)==3 and int(Day)<=20)):
        zodiac_sign = ("Pices")
    elif ((int(Month)==3 and int(Day)>=21)or(int(Month)==4 and int(Day)<=19)):
        zodiac_sign = ("Aries")
    elif ((int(Month)==4 and int(Day)>=20)or(int(Month)==5 and int(Day)<=20)):
        zodiac_sign = ("Taurus")
    elif ((int(Month)==5 and int(Day)>=21)or(int(Month)==6 and int(Day)<=20)):
        zodiac_sign = ("Gemini")



    elif((int(Month)==6 and int(Day)>=21)or(int(Month)==7 and int(Day)<=22)):
        zodiac_sign = ("Cancer")
    elif ((int(Month)==7 and int(Day)<=23)or(int(Month)==8 and int(Day)<=22)):
        zodiac_sign = ("Leo")
    elif ((int(Month)==8 and int(Day)>=23)or(int(Month)==9 and int(Day)<=22)):
        zodiac_sign = ("Virgo")
    elif ((int(Month)==9 and int(Day)>=23)or(int(Month)==10 and int(Day)<=22)):
        zodiac_sign = ("Libra")
    elif ((int(Month)==10 and int(Day)>=23)or(int(Month)==11 and int(Day)<=21)):
        zodiac_sign = ("Scorpio")
    elif ((int(Month)==11 and int(Day)>=22)or(int(Month)==12 and int(Day)<=21)):
        ozdiac_sign = ("Sagittarius")

    print (zodiac_sign)
program()
