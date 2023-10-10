class Student:
    def __init__(self, name ="N/A", age = 13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def study(self, studing):
         print(f"{self._name} is studying {studing}")
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, newName):
        if(type(newName) == str and newName != newName.isspace() and  len(newName) > 3):
                self._name = newName
    @property
    def get_age(self):
         return self._age
    
    @property
    def get_grade(self):
         return self._grade
    
    @get_age.setter
    def set_age(self, new_age):
         if(type(new_age) == int and new_age > 10 and new_age < 18 ):
             self._age = new_age
    
    @get_grade.setter
    def set_grade(self, new_grade):
         if(new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == '12th'):
              self._grade = new_grade
    
    def __str__(self):
        return f"Student: {self._name} | Age: {self._age}| Grade: {self._grade}"

studentOne = Student('alice')
print(studentOne.study('Computers'))