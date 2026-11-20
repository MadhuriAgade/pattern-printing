# Question 5: Repeated Row Number Triangle
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6):       # rows
    print(i,end=" ")       # print number
    for j in range(i-1):   # columns
        print(i,end=" ")   # print number
    print()                # next line
 