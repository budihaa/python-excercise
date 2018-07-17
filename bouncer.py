# Ask the visitor age
age = input("How old are you? ")

# checking value of age is empty
if age:
    # convert age to int
    age = int(age)
    if age >= 21:
        # 21 >= can drink
        print("You can enter and drink.")
    elif age >= 18:
        # 18 >= can enter but cannot drink
        print("You can enter but can't drink.")
    else:
        print("You are too young, little one.")
else:
    print("You must enter your age!")
