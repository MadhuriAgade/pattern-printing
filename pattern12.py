# Question 12: Butterfly Pattern
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

for i in range(5):              # rows
    for j in range(9):          # columns
        if j <= i or j >= 8-i:  # check condition
            print("*", end=" ") # print stars
        else:
            print(" ", end=" ") # print spaces
    print()                     # next line

for i in range(3, -1, -1):      # rows
    for j in range(9):          # columns
        if j <= i or j >= 8-i:  # check condition
            print("*", end=" ") # print stars
        else:
            print(" ", end=" ") # print spaces
    print()                     # next line
