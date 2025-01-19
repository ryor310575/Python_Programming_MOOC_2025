# Write your solution here
h_wage=float(input("Hourly wage: "))
h_worked=float(input("Hours worked: "))
d_week=input("Day of the week: ")
d_wage=h_wage*h_worked
if d_week=="Sunday":
    d_wage=d_wage*2
print(f"Daily wages: {d_wage} euros")