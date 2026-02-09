glosssalary = int(input("Enter your salary"))
if glosssalary > 0 and  glosssalary <= 5999:
    print("Your monthly contribution is  KSH 150000 ")
elif glosssalary > 5999 and  glosssalary <= 7999:
    print("Your monthly contribution is  KSH Ksh 300000")
elif glosssalary > 7999 and  glosssalary <= 11999:
    print("Your monthly contribution is  KSH 400000 ")
elif glosssalary > 11999 and  glosssalary <= 14999:
    print("Your monthly contribution is  KSH 500000 ")
elif glosssalary >14999  and  glosssalary <= 19999:
    print("Your monthly contribution is  KSH 600000 ")
elif glosssalary > 19999 and  glosssalary <= 24999:
    print("Your monthly contribution is  KSH 750000 ")
elif glosssalary > 24999 and  glosssalary <= 29999:
    print("Your monthly contribution is  KSH 850000 ")
elif glosssalary > 29999 and  glosssalary <= 49999:
    print("Your monthly contribution is  KSH 950000 ")
elif glosssalary > 49999 and  glosssalary <= 99999:
    print("Your monthly contribution is  KSH 10000000 ")
else :
    print("Salary is 2Milion")