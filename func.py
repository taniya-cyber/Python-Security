#Def is a keyword used to define a function; stands for Definitation
#If we want to leave a function blank as you don't have anything right now, so, we use a KEYWORD =  "pass". And () these are for passing arguements.
def hello_func():
    pass #saying we don't want error to leave this function blank.
#To call the function, parenthesis are compulsory, if we don't put them, function will not be executed.

print(hello_func) #this is not executing the function but just printing its location
print(hello_func()) #Prints None as function has nothing

#Putting some values now
def hello_func1():
    print('Hello Fuction!!')

hello_func1()

#Use Of Function: To Reuse a Code, also allows us to put a code into specific location so that if we need to change something in full, then we can change at one place. 

