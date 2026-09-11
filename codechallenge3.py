print("==========PACKAGE DETAILS==========")

Y = "YES"
N = "NO"


sdn = (input("\nSender Name:     "))
top = (input("Type Of Product:   "))

frag = (input("Fragile? (YES / NO): "))
if frag == Y:
  print("The product is Fragile")
elif frag == N:
  print("The product is Non-Fragile")
else:
  print("Unidentified")

print("\n\n==========Product Details==========")
wkg = eval(input("Weight(kg):     "))
dist = eval(input("Distance(km):  "))

basco = (wkg * 2.50) + (dist * 0.15)
print("The base cost of package: ₱",basco)

#exp = input("Express (YES / NO): ")
#if exp == Y:
 # print("Express: True")
#elif exp == N:
  print("Express: False")
#else:
  #print(exp,"UNIDENTIFIED")
wkg = eval(input("Weight(kg):     "))
dist = eval(input("Distance(km):  "))

basco = (wkg * 2.50) + (dist * 0.15)
exp = bool(input("Express (TRUE / FALSE): "))
int = bool(input("International (TRUE / FALSE): "))


if wkg<= 2 and dist<= 100:
  add = 0.00
  print("The Shipping is Free")
elif exp == True and int == True :
  add = (basco * 1.40) + 50 
elif exp == True or int == True :
  add = (basco * 1.20) + 25
elif wkg>= 30 or dist>= 1000:
  add = basco + 30
else: 
  print("The base cost of package: ₱",basco)
  
