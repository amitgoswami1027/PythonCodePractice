import random
import pandas

#List comprehension
#new_list = [new_list for item in list]

#list = [1,2,3,4,5,6,7,8]
#new_list = [item for item in list if item%2==0]
#print(new_list)

# Write program to get the common items from both the lists
with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\/NATOProject\/file1.txt", "r") as file1:
    list1 = file1.readlines()
    
with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\/NATOProject\/file2.txt", "r") as file2:
     list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2 ]
print(result)

#Dictionay Comprehension
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
Students = ["Amit", "Sumit", "Aryan", "Asha"]

student_scores = {student:random.randint(1,100) for student in Students}
#print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
#print(passed_students)

# How to Loop through Pandas DataFrames
student_dict = {
     "student" : ["Amit", "Sumit", "Bobby"],
     "score" : [ 56, 57, 58]
}

#for (key,value) in student_dict.items():
#     print(key)

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#for (key,value) in student_dataframe.items():
#     print(key)

# Each of the row is the pandas data series
for (index,row) in student_dataframe.iterrows():
     print(row)




