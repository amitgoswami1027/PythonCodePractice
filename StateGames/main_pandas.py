import os
import csv
import pandas

#Get the current working directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print(cwd)

#Concatinate the file paths
file ="\PythonCodePractice\StateGames\weather_data.csv"
current_path = cwd + file

#Print the lines
#with open(current_path,"r") as data:
#    new_line = data.readlines()
#    #print(new_line)

# Get the temerature values using the csv reader funtions
with open(current_path,"r") as data1:
    new_line1 = csv.reader(data1)
    temperatures = []
    for line in new_line1:
        if line[1] != "temp":
            temperatures.append(line[1])
            #print(line)
    
    #print(temperatures)

# Working with Pandas makes the life easy navagating the files
data = pandas.read_csv(current_path)
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(temp_list)

#Get the Data in Row
print(data[data.day == "Monday"])

print(data.temp.max())

