#welcome back, here we are again.
#Task 1
#learning how to use f-strings
pet_type = "cat"
pet_name = "Ash"
print (f"I have a {pet_type} and his name is {pet_name}.")

#Task 2
#information entered by user gets but through some processes and spat out, yay.
user_name = input("Enter your first name: ")
user_age = input("Enter your current age: ")
user_savings = input("Enter your yearly savings: ")
print (f"Hello {user_name}! You are currently {user_age}.")
#user age in 10 years
print (f"In 10 years you will be {int(user_age) + 10 }")
#user income statistics
print (f"If you save ${user_savings} per year, in 5 years you will have saved ${int(user_savings) * 5}")
#note to self, the .2f goes after the function is compete
print (f"Your average monthly savings is ${int(user_savings) / 12 :.2f}")

#Task 3
#converting days to seconds
jan_days = 31
print(f"The number of seconds in January is {jan_days * 24 * 60 * 60}")

#Task
#learning remainders in f-strings
egg_amount = input("Enter the number of eggs: ")
print(f"This makes {int(egg_amount) //12} dozen eggs with {int(egg_amount) %12} left over")