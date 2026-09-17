class Science:
    def __init__(self, name, age, grade, cob= "Belgium"):
        self.name = name
        self.age = age
        self.grade = grade
        self.cob = cob
student1 = Science("Michael", 25, 92)
student2 = Science("Debbie", 24, 93)
student3 = Science("Thomas", 99, 90, )

def main():
    print (student1.age)
    print (student2.cob)
    print (student3.cob)

#create default object fallback if unsure or if not created. e.g.: cob (country of birth)
    print("you will not see this text if import from different module is succesful")
if __name__ == "__main__":
    main()
