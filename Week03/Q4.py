mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

mondayClass.add("Grace")
print("Monday class ", mondayClass)
print("Wednesday class ", wednesdayClass)
bothClasses = mondayClass & wednesdayClass
print("Attended both classes: ", bothClasses)
allStudents = mondayClass | wednesdayClass
print("Attended either class: ", allStudents)
onlyOne = mondayClass ^ wednesdayClass
print("Attended only one class: ", onlyOne)
print("Is Monday subset of all students?", mondayClass <= allStudents)