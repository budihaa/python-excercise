# Loop 1-20
# if number = 4 & 13, print unlucky
# if number = odd, print number is odd
# if numbe = event, print number is even

for x in range(1, 21):
    if x == 4 or x == 13:
        print(f"{x} is UNLUCKY!")
    elif x % 2:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")
