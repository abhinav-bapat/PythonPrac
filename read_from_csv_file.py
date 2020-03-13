# Step-1: opening the file
courses = open('courses_list.csv')


# Step-2: Processing
for x in courses:
    print(x, end='')

# Step-3: Closing the file
courses.close()
