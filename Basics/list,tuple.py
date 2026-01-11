#Lists
courses = ['Math', 'Sci', 'Art']
course_1 = ['Hindi']
"""print(courses)
print(len(courses))
print(courses[0:])
print(courses[:-1])
print(courses[-1:]) 
courses.append(course_1) #Doesn't add elements of courses in course_1, neither insert works here.
print(courses)
courses.extend(course_1)
courses.extend(courses)
print (courses)"""
courses.remove('Math')
print (courses)
popped = courses.pop()
print (popped)