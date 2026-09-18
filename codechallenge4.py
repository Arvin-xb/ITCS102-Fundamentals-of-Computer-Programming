import getpass

t = True
f = False
print("========CREATE AN ACCOUNT=========")
sign_up = input("Enter Your Username: ")
cpassword = getpass.getpass("Enter Your Password: ")

ulogin = input("Enter Your Username: ")
apassword = getpass.getpass("Enter Your Password: ")

print("========ACCOUNT LOG IN=========")
if ulogin == sign_up:
    print("Username Correct")
    if apassword == cpassword:
        print("Password Correct")
    else:
        print("Password Incorrect")
else:
    print("Username Incorrect")

age = int(input("Enter Your Age:  "))
is_employed = bool(input("Are you employed? (True / False): "))
credit_score = eval(input("Your Credit Score:  "))
annual_income = eval(input("Your Annual Income: "))
has_collateral = bool(input("Do you have any collateral? (True / False ): "))




print("================================================")
if age >= 21 and age <= 65 and is_employed == t: #Tier1
    print("Age: Qualified\nEmployed: True")
    if credit_score>= 750:
        print("Credit Score: ",credit_score, "= Qualified")
        if annual_income >= 100000:
                base_rate = 4.5
                print("Loan Request: Approved\nInterest Rate: ",base_rate,"%")
        else:
                base_rate = 5.0
                print("Loan Request: Approved\nInterest Rate: ",base_rate,"%")                
    elif credit_score >= 600 and credit_score <750: #Tier 2
        print("Credit Score:",credit_score,"= Qualified")
        if has_collateral == t:
            base_rate = 7.0
            print("Collateral: True")
            if annual_income < 40000:
                base_rate = 9.5
                print("Loan Request: Apporved\nInterest Rate: ",base_rate,"%")                     
            else:
                print("Loan Request: Apporved\nInterest Rate: ",base_rate,"%")
        else:
            base_rate = 8.0
            print("Collateral: ",has_collateral,"\nLoan Request: Apporved\nInterest Rate: ",base_rate,"%")
    else: #Tier 3
            print("Credit Score: ",credit_score,",Too Low")
else:
    print("Loan Request: Rejected = Fails Baseline Criteria")
                  
                        
