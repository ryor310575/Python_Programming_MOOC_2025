# Write your solution here
farenheit=int(input("Please type in a temperature (F): "))
celcius=0.0
celcius=(farenheit-32)*5/9
print(f"{farenheit} degrees Fahrenheit equals {celcius} degrees Celsius")
if celcius<0:
    print("Brr! It's cold in here!")