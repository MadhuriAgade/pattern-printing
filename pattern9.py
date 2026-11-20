# Question 9: Diamond
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range(5):           # rows
    print("  " * (4-i), end="") # print spaces
    for j in range(2*i+1):   # columns
        print("*", end=" ")  # print stars
    print()                  # next line

for i in range(1,5):         # rows
    print("  " * i, end="")  # print spaces
    for j in range(9-2*i):   # columns
        print("*", end=" ")  # print stars
    print()                  # next line