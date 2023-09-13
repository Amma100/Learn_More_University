# Program to calculate student result and grade it
try:
    # prompt for user input
    Matric_Num = input("Enter Matriculation Number: ")
    Student_Name = input("Enter Student Name: ")
    Python_Score = float(input("Enter Python Score: "))
    English_Score = float(input("Enter English Score: "))
    Math_Score = float(input("Enter Maths Score: "))

    print("\nProcessing...\n")

    # calculate total and average score
    Total_Score = Python_Score + English_Score + Math_Score
    Average_Score = (Total_Score / 3)

    # verify what grade satisfies user average
    if (Python_Score or English_Score or Math_Score) < 0:
        print("\nPlease enter a positive score to get your grade!!!\n")
    elif 0 <= Average_Score <= 39:
        print("FAIL")
    elif 40 <= Average_Score <= 54:
        print("PASS")
    elif 55 <= Average_Score <= 69:
        print("CREDIT")
    elif 70 <= Average_Score <= 89:
        print("VERY GOOD")
    elif 90 <= Average_Score <= 100:
        print("EXCELLENT")
    else:
        print("\nYour average score is out of bound")

except:
    print("\nEnter correct scores in digits not words...\n")
