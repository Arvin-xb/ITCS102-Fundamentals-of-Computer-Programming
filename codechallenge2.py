#operator = symbol
#heehee

print("==================PH BANK DENOMINATION=======================")
moneytd = eval(input("Enter Money to Deposit:"))

num1 = moneytd // 1000
num2 = moneytd % 1000 // 500
num3 = moneytd % 1000 % 500 // 200
num4 = moneytd % 1000 % 500 % 200 // 100
num5 = moneytd % 1000 % 500 % 200 % 100 // 50
num6 = moneytd % 1000 % 500 % 200 % 100 % 50 // 20
num7 = moneytd % 1000 % 500 % 200 % 100 % 50 % 20 // 10
num8 = moneytd % 1000 % 500 % 200 % 100 % 50 % 20 % 10 // 5
num9 = moneytd % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 // 1

print("\n\t1000 =",num1,"\n\t500 =",num2,"\n\t200 =",num3,"\n\t100 =",num4,"\n\t50 =",num5,"\n\t20 =",num6,"\n\t10 =",num7,"\n\t5 =",num8,"\n\t1 =",num9,"\n\n Total Amount of Money Deposited:",moneytd)
