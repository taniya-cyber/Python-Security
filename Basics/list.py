"""
#Lists
courses = ['Math', 'Sci', 'Art']
course_1 = ['Hindi']
print(courses)
print(len(courses))
#Indexing and Slicing
print(courses[0:])
print(courses[:-1])
print(courses[-1:]) 
courses.append(course_1) #Doesn't add elements of courses in course_1, neither insert works here.
print(courses)
#Adding elements of one list in other
courses.extend(course_1)
courses.extend(courses)
print (courses)
courses.remove('Math') #Removes particular elements
print (courses)
popped = courses.pop() #Pops last element,, we can even make a Loop and Initialize this as function within loop = working of A stack.
print (popped)
"""
#Sorting Using List Methods. List Methods are: 1. .reverse 2. .sort 3. .sort(reverse = true) or by .sort then .reverse for Descending order
# list_1 = [1, 102, 'hO', 'hE'] DOES NOT SUPPORT INT + STR SORT.
list_1 = ['hi', 'Ab', 'Ho']
list_1.reverse()
print(list_1)
list_1.sort()
print(list_1)
#We can either sort then replace or we can do this: list_1.sort(reverse = True), this shows it in descending order.
#if we don't want to change the original list, we can do this:
sorted_l1 = sorted(list_1)
#We also have max, min and sum functions to be performed on numbers
#Checking if 'ho' is in list or not?
print ('ho' in list_1) #retuns false as 'Ho' is in list not 'ho'
#List into String by JOIN
list_1str = ', '.join(list_1) #', ' this shows we need comma and space between list items
print(list_1str)
#Now str into list: By SPLIT
new_list = list_1str.split(',')
print(new_list)