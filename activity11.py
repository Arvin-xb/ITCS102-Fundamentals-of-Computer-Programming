#Import Demo
import getpass

username = "arvino"
password = "heehee"


u = input("Enter Username: ")
p = getpass.getpass("Enter Password: ")

if u == username and p == password:
   print("Username Correct\nPassword Correct")

else: 
   print("Access Denied")

