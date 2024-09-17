try:
    age=int(input("Please enter your age: "))
except ValueError:
    print("THis is not a value response")
    
print("In one year, you will be ",age+1)