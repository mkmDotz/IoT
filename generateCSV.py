import csv


data = [

    ["EmployeeId" , "EmployeeName","JobDesription","Salary"],

    [123453,"Jack","CEO",12000]

]

data.append([1038113, "MKM", "ASE", "20000"])


with open('Test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(data)




    
    
