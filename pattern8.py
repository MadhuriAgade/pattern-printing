# Question 8: Inverted Star Pyramid
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range (5):          # rows
    print("  "*i,end ="")    # print spaces
    for j in range(9 - 2*i): # columns
        print("*",end=" ")   # print stars
    print()                  # next line