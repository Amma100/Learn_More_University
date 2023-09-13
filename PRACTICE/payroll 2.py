# python program to compute staff payroll for the month of August 2022

# get data from the user

Staff_number = input("Enter staff number: ")
Staff_Name = input("Enter staff name: ")
Position = input("Enter staff position: ")
Basic_Salary = input("Enter staff salary: ")

try:
    new_basic_salary = float(Basic_Salary)
    # declare salary range
    if 70000 <= new_basic_salary <= 200000:
        print("processing")
        # Write an if statements to get Feeding Allowance value
        if new_basic_salary > 140000:
            Feeding = (0.25 * new_basic_salary)
        else:
            Feeding = (0.15 * new_basic_salary)

        # Get the Medical Allowance value
        Medical = (0.1 * new_basic_salary)

        # Write an if statements to get Transport Allowance value
        if new_basic_salary >= 140000:
            Transport = (0.2 * new_basic_salary)
        else:
            Transport = (0.1 * new_basic_salary)

        # Write an if statements to get House Allowance value
        if new_basic_salary < 140000:
            Housing = (0.15 * new_basic_salary)
        else:
            Housing = (0.3 * new_basic_salary)

        # Get Tax value
        Tax = (0.07 * new_basic_salary)

        # Get Gross Pay
        Gross_Pay = Feeding + Medical + Transport + Housing + new_basic_salary

        # Get Net Pay
        Net_Pay = Gross_Pay - Tax

        # Give first output
        print("\n\nOutput 1\n=======\n")
        print("\t\t\tPromise Oil and Gas Limited\t\t\t\t\t\t\t\t\tCurrent Date: 11/08/2021\n\t\t\tHaruna, Ikorodu.")
        print("\n\t\t\tStaff Payroll for August 2022\n")
        print("Staff No\t\tStaff Name\t\tPosition\t\tGross Pay\t\tNet Pay\n========\t\t==========\t\t========\t\t=========\t\t=======\n{}\t\t\t{}\t\t{}\t\t{}\t\t{}\n\n".format(Staff_number,Staff_Name,Position,Gross_Pay,Net_Pay))

        # Give second output
        print("\n\nOutput 2\n=======\n")
        print("\t\t\tPromise Oil and Gas Limited\t\t\t\t\t\t\t\t\tCurrent Date: 11/08/2021\n\t\t\tHaruna, Ikorodu.")
        print("\n\t\t\tStaff Payroll for August 2022\n")
        print("Staff Details\n=============\n\nStaff number\t\t\t : {}\nStaff Name  \t\t\t : {}\nPosition    \t\t\t : {}\nBasic Salary\t\t\t : {}".format(Staff_number,Staff_Name,Position,Basic_Salary))
        print("\nPayroll Detail\n==============\n\nFeeding Allowance  \t\t\t : {}\nMedical Allowance  \t\t\t : {}\nTransport Allowance\t\t\t : {}\nHouse Allowance    \t\t\t : {}\nTax            \t\t\t\t : {}".format(Feeding,Medical,Transport,Housing,Tax))
        print("\n==============================================\nGross Pay          \t\t\t : {}\nNet Pay            \t\t\t : {}\n==============================================".format(Gross_Pay,Net_Pay))
        print("Spend your salary wisely...")

    else:
        print("Salary out of range")

except:
    print("---Error!!!---\nEnter Basic Salary in number")

