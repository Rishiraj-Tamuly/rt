''' Write a program which accepts a sequence of comma-separated numbers from console and
    generate a list. '''

lst = []
n = int(input("Enter the number of elements to be entered in the list: "))
for i in range(n):
    j = input("Enter elements: ")
    lst.append(j)
print("List = "+str(lst))
