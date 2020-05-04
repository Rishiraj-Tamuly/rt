''' Write a Python program to reverse a word after accepting the input from the user.
    Sample Output:
    Input word: AcadGild
    Output: dilGdacA '''  

x = input("Enter a word: ")
y = ""
for i in range(len(x)-1,-1,-1):
    y = y + x[i]
print("Reverse of the word: "+y)

