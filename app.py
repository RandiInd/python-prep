# from math import *


# print("Hello")
# print(ceil(2.3))
# friends = ["Levi", "James", True]
# print(friends[-1])
# print("Kevin")
# month_conversions = {
#     "Jan" : "January",
#     "Feb" : "February"

# }

# print(month_conversions["Mar"]) # can use .get function of dictionary to insert default value
# print(month_conversions.get("Mar", "Not exist"))
# for index in range(1, 8): 
  #   print(index ** index)   # test

# number_grid = [
#     [1, 3, 8],
#     [2, 4],
#     [0]
# ]

#print(number_grid[0][0])

# for row in number_grid:
   # for col in row:
    #    print(col)


# def translater(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             translation += "g" 
#         else:
#             translation += letter
#     return translation

# print(translater(input("enter a phrase: ")))

# try:
#     number = int(input("Enter a number"))
#     print(number)
# except:
#     print("Invalid")

# python_file = open("sample file.txt", "r")
# print(python_file.readline())
# for line in python_file.readlines():
#     print(line)
# python_file.close()

# python_file = open("C:/Ruwandi/Dev/Python/Python Coding Standard.docx", "r")
# python_file.readline()

# python_file.close()


# from Student import Student    # from Student file import Student class
# from ExternalStudent import ExternalStudent

# student_new = Student("Kelly", "Business", 3.1, False)
# print(student_new.name + ' in special degree ? ' + str(student_new.on_special_degree()))

# external_student = ExternalStudent("Glen", "Business", 3.6, False, 3000)
# print(external_student.name + ' in special degree ? ' + str(external_student.on_special_degree()))
# print(external_student.name + "'s degree fee is = " + str(external_student.get_class_fee()))

# mylist = [1,2,3,4,5]

# print(mylist[::-1])

# import tracemalloc
# from Student import Student
# tot_iteration = 100
# def mem_testing_method():
#     for i in range(tot_iteration):
#         new_student = Student("Glen", "Business", 3.5, True)
#         print(new_student.on_special_degree())
# def mem_testing_method2():
#     new_student = Student("Glen", "Business", 3.5, True)
#     print(new_student.on_special_degree())
#     new_student1 = Student("Glen1", "Business", 3.5, True)
#     print(new_student1.on_special_degree())
#     new_student2= Student("Glen2", "Business", 3.5, True)
#     print(new_student2.on_special_degree())
#     new_student3 = Student("Glen3", "Business", 3.5, True)
#     print(new_student3.on_special_degree())
#     new_student4 = Student("Glen4", "Business", 3.5, True)
#     print(new_student4.on_special_degree())
#     new_student5 = Student("Glen3", "Business", 3.5, True)
#     print(new_student5.on_special_degree())
#     new_student6 = Student("Glen", "Business", 3.5, True)
#     print(new_student6.on_special_degree())
#     new_student7 = Student("Glen", "Business", 3.5, True)
#     print(new_student7.on_special_degree())
#     new_student8 = Student("Glen", "Business", 3.5, True)
#     print(new_student8.on_special_degree())
#     new_student9 = Student("Glen", "Business", 3.5, True)
#     print(new_student9.on_special_degree())
#     new_student10 = Student("Glen", "Business", 3.5, True)
#     print(new_student10.on_special_degree())
#     new_student11 = Student("Glen", "Business", 3.5, True)
#     print(new_student11.on_special_degree())
#     new_student12 = Student("Glen", "Business", 3.5, True)
#     print(new_student12.on_special_degree())
#     new_student13 = Student("Glen", "Business", 3.5, True)
#     print(new_student13.on_special_degree())
#     new_student14 = Student("Glen", "Business", 3.5, True)
#     print(new_student14.on_special_degree())

# tracemalloc.start()
# mem_testing_method()
# current, peak = tracemalloc.get_traced_memory()
# print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
# tracemalloc.stop()

# tracemalloc.start()
# mem_testing_method2()
# current, peak = tracemalloc.get_traced_memory()
# print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
# tracemalloc.stop()


add10 = lambda x: x + 10  #lambda function

print(add10(5))


mylist = [1,2,3,4,5]

print(mylist[::-1])
