#break statement:

for i in range(1, 6):
    if i == 3:
        break
    print(i)

#pass statement:

for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)

#continue statement:

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#for loop with else statement:

for i in range(1, 6):
    print(i)
else:
    print("Loop completed")

#while loop with else statement:

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")




