''' Write a Python program to accept the user's first and last name and then getting them printed in
    the the reverse order with a space between first name and last name.
'''

# 1st method
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
st = ""
sp = ""
for i in range(len(first_name)-1,-1,-1):
    st = st + first_name[i]
for j in range(len(last_name)-1,-1,-1):
    sp = sp + last_name[j]
print("Reverse of first name and last name is: "+st+" "+sp)


# 2nd method
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
ps = first_name[::-1]
pq = last_name[::-1]
print("Reverse of first name and last name is: "+ps+" "+pq)





   
