message = ("Welcome to the salary calculator based on your worked hours")
print(message)
print("We are going to calculate your salary depending on the hours worked and your job position")
print("Remember that the available positions are 1-Manager 2-SubManager 3-Supervisor 4-Employee 5-Intern")
print("When we ask for your position, please answer with the number")
name = input("Enter your name: ")
age = input("Enter your age: ")
major = input("Enter your major: ")
student_id = input("Enter your student ID: ")
worked_hours = int(input("Enter your worked hours: "))
job_position = int(input("Enter your job position: "))

if job_position == 1:
    salary = worked_hours * 50
    monthly_salary = salary * 4
elif job_position == 2:
    salary = worked_hours * 40
    monthly_salary = salary * 4
elif job_position == 3:
    salary = worked_hours * 30
    monthly_salary = salary * 4
elif job_position == 4:
    salary = worked_hours * 20
    monthly_salary = salary * 4
elif job_position == 5:
    salary = worked_hours * 10
    monthly_salary = salary * 4
else:
    print("Error: Invalid job position entered.")

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.text(10, 20, "Name: " + name)
pdf.text(10, 30, "Age: " + age)
pdf.text(10, 40, "Major: " + major)
pdf.text(10, 50, "Student ID: " + student_id)
pdf.text(10, 60, "Worked hours: " + str(worked_hours))
pdf.text(10, 70, "Weekly salary: $" + str(salary))
pdf.text(10, 80, "Monthly salary: $" + str(monthly_salary))

pdf.output("Salary.pdf")
print("Payroll receipt generated!! Check the generated PDF!!")
