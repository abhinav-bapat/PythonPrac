# Step-1: opening the file
courses = open('courses_list.csv', 'w')


# Step-2: Processing
print('Python Basics', file=courses)
print('Python Intermediate', file=courses)
print('Spring Core', file=courses)
print('Spring MVC', file=courses)


# Step-3: Closing the file
courses.close()


