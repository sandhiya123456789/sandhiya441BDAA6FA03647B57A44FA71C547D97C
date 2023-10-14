def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
   if product == targetProduct:
     indices.append(index)
  return indices
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
[24/09, 9:20 pm] +91 94435 19499: class Student:
   def __init__(self, name, roll_number, cgpa) :
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key = lambda student:student.cgpa, reverse = True) 
  return sorted_students
students = [Student("Hari", "A123", 7.8), Student(" Srikanth", "A124", 8.9) , Student("Saumya", "A125",9.1), Student ("Mahidhar", "A126",9.9) ]
sorted_students = sort_students(students) 
for st