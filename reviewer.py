

print("SMALL BUSINESS LOAN APPLICATION")
owner_age = int(input("Enter your Age: "))
monthly_revenue = float(input("Enter your Monthly Revenue: "))
credits_score = float(input("Enter your Credit Score: "))
years_in_business = float(input("Enter your Years in Business: "))
has_default = bool(input("Do you have any defaults? (True/False): "))
collateral = (input("Valuable Thing to collat: "))
collat_val = float(input("Collateral Value: "))


max_limit = 0
base_fee = 0

if owner_age >= 21 and years_in_business >= 2.0 and has_default == False:
    print("Baseline Requirements Met: Eligible for Loan Application")
    if credits_score >= 720: #tier 1
        max_limit = monthly_revenue * 3
        print("Approved\nMaximum Loan Limit: $", max_limit)
        if monthly_revenue >= 50000:
            base_fee = max_limit * 0.015
            print("Base Fee: $", base_fee)
        else:
            base_fee = max_limit * 0.025
            print("Base Fee: $", base_fee)
        
        if collat_val % 5000 != 0:
            surcharge += 250
                    
    elif credits_score <= 620 and credits_score < 719: #tier 2
        max_limit = monthly_revenue * 1.5
        print("Approved\nMaximum Loan Limit: $", max_limit)
        if years_in_business >= 5.0:
            base_fee = max_limit * 0.02
            print("Base Fee: $", base_fee)
        else:
            base_fee = max_limit * 0.035
            print("Base Fee: $", base_fee)
        
        if collat_val >= max_limit:
            print("Collateral: ",collat_val,"= Accepted")
        else:
            print("Collateral: ",collat_val,"= Rejected")     
    else: #tier 3
        print("Loan Denied: Credit score too low.")
else:
    print("Loan Denied: You do not meet the baseline requirements for a loan application.")
