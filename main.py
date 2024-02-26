print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nwelcome to my Age Calculator App\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
name = input("please enter your name: ")
print(f"hello {name}")
while True:
    age = input("please enter your age: ").strip()
    unit = input("please enter the unit[months or m,weeks or w,days or d]: ").strip().lower()

    months = int(age) * 12
    weeks = months * 4
    days = int(age) * 365

    if unit == "months" or unit == "m":
        print(f"you lived for {months:,} months")
    elif unit == "weeks" or unit == "w":
        print(f"you lived for {weeks:,} weeks")
    elif unit == "days" or unit == "d":
        print(f"you lived for {days:,} days")
    else:
        print("this option is not in the list!")
        quit()

    ask = input("do you want to calculate any age again [yes,no]: ").strip().lower()
    if ask == "yes":
        continue
    elif ask == "no":
        print(f"ok {name} have a nice day:)")
        break
    else:
        break
# this is my Age Calculator App



