class person:
    def __init__(self,name,age,semester,cgpa):
        # pass       #if you want to define something but not implement it yet, you use pass.
        self.name = name
        self.age = age
        self.semester = semester
        self.cgpa = cgpa

    def __str__(self):   #__str__ is a special (or “dunder”) method in Python that defines how your object should look when you print it.
        return f"{self.name},Age:{self.age},Semester:{self.semester},cgpa:{self.cgpa}"     #“This is an f-string, so Python should evaluate any expressions inside {} and insert their values directly into the string.”

p1 = person("faisal",21,5,7)
p2 = person("Suhail",20,5,5)
p3 = person("Junaid",21,5,9)
p4 = person("Hashim",22,5,8)
p5 = person("Najma",21,5,6)


personsList = list((p1,p2,p3,p4,p5))
for student in personsList:
    if student.cgpa>7 or student.cgpa == 7:
        print(student)


#inheritance 
class person2(person):     # inherited properties from the above person class without even writing in this class
    pass

p0 = person2("Rakia",22,5,9)
print(p0)
