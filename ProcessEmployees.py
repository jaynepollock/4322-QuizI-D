'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open('employee_data.csv','r')
reader = csv.reader(infile, delimiter = ",")
next(reader)


#create an empty dictionary
saldict = {}

#use a loop to iterate through the csv file
for row in reader:
    idnum = row[0]
    fname = row[1]
    lname = row[2]
    dpt = row[3]
    title = row [4]
    salary = int(row[5])
    hiredate = row[6]
    bday = row[7]
    gender = row[8]
    clearance = row[8]


    #check if the employee fits the search criteria
    current_salary = 0
    if dpt == "Marketing" or "Management":
        future_salary = salary * 1.10
        cursal = ("Manager name: " + fname + lname + " Current Salary: "+'$' + str(round(salary,2)))
        newsal = ("Manager name: " + fname + lname + " New Salary: "+'$' + str(round(future_salary,2)))
    
        
    
    saldict = {fname: round(future_salary, 2)}

    
    print(cursal)
    print(newsal)


print()
print('=========================================')
print()

    
#iternate through the dictionary and print out the key and value as per printout


print(saldict)
for k, v in saldict.items():
    print("Manager name: " +str(k) + " New salary: "+ '$' +str(v))



        
    
