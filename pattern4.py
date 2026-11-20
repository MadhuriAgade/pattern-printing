# Question 4: Increasing Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):       # rows
    for j in range(1,i+1): # columns
        print(j,end=" ")   # print numbers
    print()                # next line
   