class Person:
  pass       # is used to bypass the error if the class is empty and you don't want any error then you can use pass keyword and then it will not give any error 
  def __init__(self,name,age,skill):
    self.name=name
    self.age=age
    self.skill=skill
  def printing(p):
    print(p.name)
    print(p.age)
    print(p.skill)
person1= Person("faisal",22,"webDeveloper")
person2= Person("arsalan",24,"ProjectCoordiantor")

Person.printing(person1)
Person.printing(person2)



