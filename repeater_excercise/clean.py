# Create program that print "CLEAN YOUR ROOM" based on user input

loops = input("How many time i must tell you? ")

# klo langsung masuking angka di dalem range maka, range akan sesuai angkanya
# misalnya loopnysa 3 -> range(3) -> range(0, 3)
for x in range(int(loops)):
    print("CLEAN YOUR ROOM")
