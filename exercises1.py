height = float(input("Enter meters: "))
weight = float(input("Input kilogram: "))
BMI = (weight / ((height * height)/10000))
print (BMI)
if BMI < 16:
    print ("Severely underweight")
elif BMI < 18.5:
    print ("Underweight")
elif BMI < 25:
    print ("Normal")
elif BMI < 30 :
    print ("Overweight")
else:
    print("Obese")