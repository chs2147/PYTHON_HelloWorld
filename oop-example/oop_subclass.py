class SchoolMember:
    '''Represents any school member.'''

    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "(Initialized SchoolMember: {0})".format(self.name)

    def tell(self):
        """Tell my details."""
        print 'Name:"{0}" Age:"{1}"'.format(self.name,self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''

    salary = 0

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)

        self.salary = salary
        print '(Initialized Teacher: {0})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    '''Represents a student.'''

    marks = 0

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)

        self.marks = marks
        print '(Initialized Student: {0})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)


t = Teacher('Mrs. Jenny', 31, 50000)
s = Student('Mr. Leslie', 39, 95)

# Prints a blank line
print

members = [t,s]

for member in members:
    # Works for both Teachers and Students
    member.tell()


