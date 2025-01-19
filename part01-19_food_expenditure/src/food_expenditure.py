# Write your solution here
coffe_times=int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price=float(input("The price of a typical student lunch?"))
groceries_weekly=float(input("How much money do you spend on groceries in a week?"))
coffe_weekly=coffe_times*lunch_price
food_weekly=coffe_weekly+groceries_weekly
print("Average food expenditure:")
print(f"Daily: {food_weekly/7} euros")
print(f"Weekly: {food_weekly} euros")