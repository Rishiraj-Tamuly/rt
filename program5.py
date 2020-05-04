''' Create the below pattern using nested for loop in Python.
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *

    *    '''

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for m in range(5,1,-1):
    for n in range(m-1,0,-1):
        print("*",end=" ")
    print()
