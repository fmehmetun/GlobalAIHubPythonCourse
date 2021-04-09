# 1 - Course Grade App

newStudentCount = 5
studentsDict = {}

# Checks if given variable is number and between 0-100
def isGradeValid(grade):
	try:
		# Turn to integer
		grade = int(grade)
		# Check limits
		return (grade >= 0 and grade <= 100)
	# Invalid if any error occurs
	except:
		return False

# Tries to get input between 0-100 until valid.
def getGradeInput(inputText):
	while True:
		grade = input(inputText)
		if isGradeValid(grade):
			return grade
		else:
			print("[!] Invalid input!")

# Calculates course grade.
def calculateCourseGrade(midterm, project, final):
	# Check all grades if valid or not
	if (isGradeValid(midterm) and isGradeValid(project) and isGradeValid(final)):
		return (midterm * 0.3) + (project * 0.3) + (final * 0.4)

# Get student records from user.
for newStudent in range(newStudentCount):
	print("\n----- Student %d -----" % (newStudent+1))
	name = input("[?] Name: ")

	# Get grades by special function.
	midtermGrade = int(getGradeInput("[?] Midterm grade: "))
	projectGrade = int(getGradeInput("[?] Project grade: "))
	finalGrade = int(getGradeInput("[?] Final grade: "))

	# Calculate course grade.
	courseGrade = calculateCourseGrade(midtermGrade, projectGrade, finalGrade)

	# Store student infos in a dict, place it in dictionary.
	studentsDict[newStudent] = {
		"name": name,
		"midtermGrade": midtermGrade,
		"projectGrade": projectGrade,
		"finalGrade": finalGrade,
		"courseGrade": courseGrade
	}

# Get course grades in list, sort, reverse (for high-to-low grade) and print it.
courseGrades = [student["courseGrade"] for studentId, student in studentsDict.items()]
courseGrades.sort()
courseGrades.reverse()
print(courseGrades)
