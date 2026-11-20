# Question 7: Star Pyramid
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range (0,5):         # rows
    print("  "*(5-i),end=" ") # print spaces
    for j in range(2*i+1):    # columns
        print("*",end =" ")   # print stars
    print()                   # next line

