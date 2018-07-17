# Create emoji from 1 to 10 row

# for x in range(1, 11):
#     print("\U0001f600" * x)

# times = 1
# while times < 11:
#     print("\U0001f600" * times)
#     times += 1

# Whitout String Multiplication - ugly solution for python
for x in range(1, 11):
    count = 1
    star = ""
    while count <= x:
        star += "\U0001f600"
        count += 1
    print(star)
