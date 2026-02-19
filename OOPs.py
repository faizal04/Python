from abc import ABC, abstractmethod


class person:
    def __init__(self,name,age,semester,cgpa,phoneNumber):
        # pass       #if you want to define something but not implement it yet, you use pass.
        self.name = name
        self.age = age
        self.semester = semester
        self.cgpa = cgpa
        self.__phoneNumber = phoneNumber    #private but not 100%      ####   Encapsulation  ###
      
    def __str__(self):   #__str__ is a special (or “dunder”) method in Python that defines how your object should look when you print it.
        return f"{self.name},Age:{self.age},Semester:{self.semester},cgpa:{self.cgpa}"     #“This is an f-string, so Python should evaluate any expressions inside {} and insert their values directly into the string.”
    def greet(self):
        return f"hi! i am {self.name} and My Age is {self.age}"





p1 = person("faisal",21,5,7,9797115131)

p2 = person("Suhail",20,5,5,8825055921)
p3 = person("Junaid",21,5,9,123456789)
p4 = person("Hashim",22,5,8,8899772134)
p5 = person("Najma",21,5,6,9541744161)


###################### printing Values #################

# print(p2._person__phoneNumber)   # the way we can access even the private variable. 

# personsList = list((p1,p2,p3,p4,p5))
# for student in personsList:
#     if student.cgpa>7 or student.cgpa == 7:
#         print(student)



###########   Inheritance     #########

class CseBatch2023(person):
    pass

student1= CseBatch2023("Aidah",52,5,8,789678678)
print(student1)



#################   Polymorphism    ####################
# the same method name behaves differently depending on which object calls it

print(person.greet(student1))
print(person.greet(p1))
print(person.greet(p2))
  ## same greet method but behaves or passes output differently

  ##################   Abstraction    ##################
  # user has NO idea what's happening inside these methods
# they just call a simple method and get the result
# all complexity is hidden

class UniversitySystem(ABC):

    @abstractmethod
    def calculate_fee(self):
        pass
    

class CSEBATCH(person,UniversitySystem):
    def calculate_fee(self):
      basefee = 31000
      busfee = 14400
      if self.semester>5:
          basefee+=5000
      return f"the total fees is {basefee+busfee}"
    
student1 = CSEBATCH("HashimMalik",23,6,9,9889978488758)
student1 = CSEBATCH("FaisalHarray",22,5,6,983738488758)

print(student1.calculate_fee())






class Car:
    def __init__(self,brand, model,year):
        self.brand = brand
        self.model =model
        self.year=year
    def __str__(self):
        return f"brandName {self.brand}, model:{self.model}"
car1 = Car("BMW",2020,2026)
car2 = Car("Audi",2020,2026)
car3 = Car("Gwagonr",2020,2026)
car4 = Car("Aeroplane",2020,2026)

