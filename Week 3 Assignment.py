#task 1
#input user name
user_name = input("What is your name? ")
print (f'Hello {user_name}')

#task 2 and 3
#user age input to an integer
#error happens because user age is input as a string not an interger value. Strings cannot be operated on. use int 
user_age = int(input('What is your age? '))
#I combined task 2 and 3 using an f-string rather than concatonating
print(f'In five years will be {user_age + 5} years old ')

#task 4
#values that might be floating points
hours_worked = float(input('Enter the nmber of hours worked this week: '))
hourly_pay = float(input('Enter your hourly wage, without the $ symbol: '))

#task 5
#operating on values again?
print (f'Your gross pay this week is: ${hourly_pay * hours_worked:.2f} ')
#for annual pay multiply by 52(how many weeks in a year)
print (f'Your estimated annual gross pay will be ${hourly_pay * hours_worked * 52:.2f}')

