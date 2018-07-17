# Create program that print "CLEAN YOUR ROOM" based on user input

loops = input("How many time i must tell you? ")
loops = int(loops)

for x in range(loops):
    print("CLEAN YOUR ROOM")
    if x >= 5:
        print("How many times do i have to tell you!")
        break
