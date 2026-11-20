# Question 6: Right-Aligned Triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range (0,6):        # rows
    print("  "*(5-i),end="") # print spaces
    for j in range(i):       # columns
        print("*",end=" ")   # print stars
    print()                  # next line
