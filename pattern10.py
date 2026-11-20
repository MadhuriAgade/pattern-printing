# Question 10: Hollow Square
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(5):              # rows
    for j in range(5):          # columns
        if i == 0 or i == 4 or j == 0 or j == 4: # check border
            print("*", end=" ") # print stars
        else:
            print(" ", end=" ") # print spaces
    print()                     # next line
