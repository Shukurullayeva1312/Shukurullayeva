universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
Student = []
tuition = []
for row in universities:
        Student.append(row[1])
        tuition.append(row[2])
def enrollment_stats():
    print('Total students: ', sum(Student))
    print('Total tuition: $', sum(tuition))
def stud():    
    Student.sort()
    tuition.sort()
    if len(Student) % 2 == 1:
        i = round(0.5 * len(Student))
        median = Student[i-1]
    else:
        i = round(0.5 * len(Student))
        median = (Student[i-1]+ Student[i]) * 0.5
    mean = sum(Student)/ len(Student)
    print('Student mean: ', round(mean, 2))
    print('Student median: ', median)
def tui():
    tuition.sort()
    if len(tuition) % 2 == 1:
        i = round(0.5 * len(tuition))
        median = tuition[i-1]
    else:
        i = round(0.5 * len(tuition))
        median = (tuition[i-1]+ tuition[i]) * 0.5
    mean = sum(tuition)/ len(tuition)
    print('Tuition mean: $', round(mean, 2))
    print('Tuition median: $', median)

enrollment_stats()
stud()
tui()