class Person():
    def __init__(self, name, surname, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return (f"\nHi, I'm {self.name} {self.surname} and I'm {self.age} years old.")
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if len(name) < 3:
            while True:
                print("\nNames with alteast 3 characters are accepted")
                name2 = input("Please try again: ")
                if len(name2) >= 3:
                    self.__name = name2
                    break
                else:
                    continue
        else:
            self.__name = name

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, surname):
        if len(surname) < 3:
            while True:
                print("\nSurnames with alteast 3 characters are accepted")
                surname2 = input("Please try again: ").lower().capitalize()
                if len(surname2) >= 3:
                    self.__surname = surname2
                    break
                else:
                    continue
        else:
            self.__surname = surname

    @property
    def age(self):
        return self.__age
    
    @age.setter  
    def age(self, age):
        if age not in range (0, 130):
            while True:
                print("\nAge has to be between 0 and 130")
                age2 = int(input("Please try again: "))
                if age2 in range(0, 130):
                    self.__age = age2
                    break
                else: 
                    continue
        else:
            self.__age = age


class Student(Person):
    def __init__(self, name, surname, age: int, fieldOfStudy, studentBook):
        super().__init__(name, surname, age)
        self.fieldOfStudy = fieldOfStudy
        self.studentBook = studentBook

    def __str__(self):
        return (f"\nHi, I'm {self.name} {self.surname} and I'm {self.age} years old. I'm an employee.\n" \
                f"I study {self.fieldOfStudy}.\n")
    
    def printSchoolSubjects(self):
        for subject, grade in self.studentBook.items():
            print(subject, ': ', grade)
    
class Employee(Person):
    def __init__(self, name, surname, age: int, jobTitle, skills):
        super().__init__(name, surname, age)
        self.jobTitle = jobTitle
        self.skills = skills
        
    def __str__(self):
        return (f"\nHi, I'm {self.name} {self.surname} and I'm {self.age} years old. I'm an employee.\n" \
                f"I'm {self.jobTitle}.\n")
    
    def printList(self):
        print("My skills are: \n")
        for i in range(0, len(self.skills)):
            print(f"{skills[i]}")
    
if __name__ == "__main__":
    name = input("Please enter a name: ").lower().capitalize()
    surname = input("Please enter a surname: ").lower().capitalize()
    age = int(input("Please enter an age: "))
    print("Are you an employee or a student? \n1. Student \n2. Employee")
    choice = input("\nPlease select a number: ")
    if choice == "1":
        fieldOfStudy = input("Please enter your field of study: ").lower()
        studentBook = {}
        n = int(input("Please enter number of school subjects you want to add: "))
        for i in range(0, n):
            subject = input("\nPlease enter a school subject: ").lower().capitalize()
            grade = input("Please enter your grade for this subject: ")
            studentBook[subject] = grade
        userCreatedPerson = Student(name, surname, age, fieldOfStudy, studentBook)
        print(userCreatedPerson)
        userCreatedPerson.printSchoolSubjects()
    else:
        jobTitle = input("Please enter your job title: ")
        skills = []
        n = int(input("Please enter number of skills you want to add: "))
        for i in range(0, n):
            element = input("Write your skill: ").lower().capitalize()
            skills.append(element)
        userCreatedPerson = Employee(name, surname, age, jobTitle, skills)
        print(userCreatedPerson)
        userCreatedPerson.printList()

    


