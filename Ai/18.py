student = ["Aliya","Ayesha","Sumayya"]
passed = ["Aliya"]
def is_std(name):
    return name in student
def is_pass(name):
    return name in passed
for name in student:
    print("Student Name:" ,name)
    print("is a Student:" ,is_std(name))
    print("Is passed:" ,is_pass(name))
   