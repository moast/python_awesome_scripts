#1-Write an empty class declaration for a class named Student
#2-Declare five instance avriables in the class from part (1). 
#A string variable for teh first name, a string variable for the last name and three double variables that are used to store a student's exam grades.
#3- declare a constructor that takes five paameters. Use these parameters to initialize the instance variable declared earlier.
#4-Include getters and setters for each instance variable
#5-include getAvarage method to calculate and return the avarage of three exam grades


#Note: unlike java, in python you cannot have muliple constructors.
#However, you can set default values as follows


class Class(object):

	def __init__(self,students=[],className=""):
	    self.students = students
	    self.className = className
	def setClassName(self,className):
	    self.className = className    
	def getClassName(self):
	    return self.className

	def getClassAvarage(self):
		students = self.students
		totalGrades = 0
		for student in students:
			totalGrades += student.getNumericalGrade()
		return totalGrades/len(students)	    


class Student(object):
	def __init__(self,studentInfo={}):
		self.studentInfo = studentInfo

	def getAvarage(self,exam_list):
		total=0
		if len(exam_list) > 0:
			for grade in exam_list:
			    total += grade
			return total/len(exam_list)
		else:
		    return 0

	def getNumericalGrade(self):
	    homeworks = self.studentInfo["homeworks"]
	    homeworkAvarage = self.getAvarage(homeworks)
	    quizes = self.studentInfo["quizzes"]
	    quizAvarage = self.getAvarage(quizes)
	    tests = self.studentInfo["tests"]
	    testAvarage = self.getAvarage(tests)

	    return  homeworkAvarage + quizAvarage  + testAvarage

	def getLetterGrade(self):
		totalGrade = self.getNumericalGrade()
		if totalGrade > 90:
			return "A"
		elif totalGrade > 80:
			return "B"
		elif totalGrade > 70:
			return "C"
		elif totalGrade > 60:
			return "D"
		else:
		    return "F"


lloyd = Student({
    "firstName": "Lloyd",
    "lastName": "Noo",
    "homeworks": [25, 20, 25, 25],
    "quizzes": [20,18,25,22],
    "tests": [50,49]
})

alice = Student({
    "firstName": "Alice",
    "lastName": "Foo",
    "homeworks": [25,20,23,22],
    "quizzes": [19,23,19,21],
    "tests": [45,42]
})

tyler = Student({
    "firstName": "Tyler",
    "lastName": "Brett",
    "homeworks": [20,17,20,25],
    "quizzes": [10,15,25,24],
    "tests": [49,43]
})


NeuroscienceClass = Class([lloyd,alice,tyler],"Neuroscience")
print("Student:",lloyd.studentInfo["firstName"], lloyd.studentInfo["lastName"])
print("Final Grade:",str(lloyd.getNumericalGrade())," - ",lloyd.getLetterGrade())
print("Class avarage:",NeuroscienceClass.getClassAvarage())



