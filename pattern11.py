# Question 11: Hollow Right-Angled Triangle
# *
# * *
# *   *
# *     *
# * * * * *

for i in range(5):              # rows
    for j in range(i+1):        # columns
        if j == 0 or j == i or i == 4: # check border
            print("*", end=" ") # print stars
        else:
            print(" ", end=" ") # print spaces
    print()                     # next line
