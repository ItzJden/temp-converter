#STARTING POINT
print("Welcome to Temperature Converter!")


#Input Section

answer = float(input("Whats the temperature?"))
answer2 = input("Celsius or Fahrenheit? (c/f)")



#if/elif

if answer2 == "c":
    F = answer * 9/5 +32
    print(f"{answer}°C is {round(F, 2)}°F")


elif answer2 == "f":
     C = (answer - 32) * 5/9
     print(f"{answer}°F is {round(C, 2)}°C")

else:
    print("answer is invalid..")