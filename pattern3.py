# Question 3: Inverted Right-Angled Triangle
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5,-1,-1):      # rows
    for j in range(-1,i-1):   # columns
        print("*",end =" ")   # print stars
    print()                   # next line