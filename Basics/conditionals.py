#1st example of execution of if statement
password = 'weak'
if password == 'weak':
    print('Change password, its weak')
else:
    print('You have a strong password')

#2nd example of this:

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in: #or we can say: if not logged_in, print("LOG iN"), else, print("Welcome")
    print('Admin Page Opened')
else:
    print('Invalid Creds')    

#3rd part By "is" = OBJECT OPERATOR, this is to show that two objects can be same but not in same memory location.
#example 3.1:
a = [1,2,3]
b = [1,2,3]
print(a==b) #It tells if true or false, and its true.
print(a is b) #is false, as memory location is not same as they are two different objects.
#Printing memory locations of BOTH a and b.
print(id(a)) 
print(id(b))

#for the below code:
c = [2,3,9]
d = c
print(d is c) #prints if its true or false

#Some false conditions: 
#By default, if is for true and else block is for false.
condition = False
if condition:
    print('Condn true')

else:
    print('condn false')

#if Condition = None, by default, it is false. 
# If condn is = {} or [] or set() or () or '' (empty string), its also false.
# If condn is equal to 0, its also false by default. 
