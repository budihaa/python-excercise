# when user input "stop copying me" the loops end

copy = input("Lets play !: ")
copy = str(copy)
while copy != "stop copying me":
    print(copy)
    copy = str(input())
print('Okey you win.')
