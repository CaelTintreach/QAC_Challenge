firstName = str(input("Input first name: "))
lastName = str(input("Input last name: "))
homeworkMark = int(input("Input homework mark: "))
assessmentMark = int(input("Input assessment mark: "))
examMark = int(input("Input exam mark: "))

def grader (homeworkMark, assessmentMark, examMark):
    markTotal = (homeworkMark * 4) + (assessmentMark * 2) + examMark
    return markTotal

gradedMark = ((grader(homeworkMark, assessmentMark, examMark)/300) *100)

print(firstName + " " + lastName)
print(gradedMark)

if gradedMark >= 80:
    print ("A+")
elif gradedMark >= 70:
    print ("A")
elif gradedMark >= 60:
    print ("B+")
else:
    print ("Discarded")