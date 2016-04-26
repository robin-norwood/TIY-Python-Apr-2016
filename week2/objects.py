def func(arg1):
    return arg1

class Void:
    pass

# str is also a class

myName = str("Robin")
# myName is a an Object of class 'str'

sadness = Void()
# sadness is an Object of class 'Void'
hapiness = Void()
# print(type(sadness))

class Color:
    def __init__(self, clr):
        """__init__ is the function called when we instantiate an Orange by calling Orange()"""
        self.value = str(clr)

    def upcase(self):
        return self.value.capitalize()

o = Color("orange")
b = Color("blue")
c = Color(None)
#print(c.value)


# 'as if':
# o = <new Color>
# Color.__init__(o, "orange")

#o.value = "orange"
#o.frankenstein = [1, 2, 3, 4]
#print(o.upcase())

# as if: Color.upcase(o)

class Student:
    def __init__(self, firstName=None, lastName=None, GPA=None):
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA

    def isComplete(self):
        return bool(self.firstName and
                    self.lastName and
                    self.GPA is not None)

    GPAPrecision = 2
    isEnrolled = False

    @classmethod
    def roundGPA(cls, GPA):
        return round(GPA, cls.GPAPrecision)


s = Student("Robin", "Norwood", 0.0)
print(s.firstName)
print(s.isComplete())

# student = {"firstName": "Robin", "lastName": "Norwood", "GPA": 4.0}
# def isComplete(student): return bool(...)

students = [Student(), Student("Robin", "Norwood", 3.13123)]

students[0].firstName = "Joe"
students[0].lastName = "Smith"
students[0].GPA = 3.6

for student in students:
    if not student.isComplete():
        continue


    print("Name: {0} {1}".format(student.firstName, student.lastName))
    print("GPA: {0}".format(student.roundGPA(student.GPA)))

class EnrolledStudent(Student):
    isEnrolled = True
    pass

students.append(EnrolledStudent("Mac", "MacDonaldson", 3.0))

for s in students:
    print(s.firstName)
    if s.isEnrolled:
        print("Is Enrolled")
    else:
        print("Is not enrolled")

    s.GPA = float(input("Enter GPA: "))

for s in students:
    print("{0}'s GPA is {1}".format(s.firstName, s.GPA))
