## Birthday Program Calculator


### Question:
**Birthday Program
The code provided is a simple Python application that prompts a user for their birthdate, calculates the number of days until their next birthday (or the number of days since, if it has
already occurred this year), and then prints out a message to the user with this information. Here is a breakdown of the code:
 - 1. Importing the datetime module:The code starts by importing the datetime module, which provides classes for manipulating dates and times.
 - 2. print_header function:This function prints out a simple text-based header for the app, with no parameters and no return value. It's a cosmetic feature to make the console output look more presentable.
 - 3. get_birthday_from_user function:This function prompts the user to enter their birth year, month, and day, one at a time. It then uses these inputs to create
     - a datetime.date object representing the user's birthday, which it returns.
 - 4. compute_days_between_dates function:This function takes two datetime.date objects as parameters: original_date (the user's birthday) and target_date (today's date). It calculates the user's birthday for the current year by using the year from target_date and the month and day from original_date. It then subtracts target_date from this date to find the difference in days, which could be negative if the birthday has already occurred this year, positive if it's yet to come, or zero if it's today. The function returns the number of days as an integer.
 - 5. print_birthday_information function:This function takes an integer (days) which represents the number of days to or since the user's birthday. It prints out a message to the user:
     • If days is less than 0, it prints out that the user's birthday occurred days ago this year.
     • If days is greater than 0, it informs the user that their birthday is days in the future.
     • If days is 0, it wishes the user a "Happy birthday!!!"
 - 6. main function:This function orchestrates the flow of the program by calling the functions defined above in sequence:
     • It prints the header.
     • It gets the user's birthday and stores it in the variable bday.
     • It fetches the current date and stores it in the variable today.
     • It computes the number of days between the user's birthday and the current date.
     • It then prints the birthday information (how long until the user's birthday, or how long since).
 - 7. Calling main:At the end of the code, main() is called, which starts the execution of the program logic.
When run, the program will display the app header, ask the user for their birthday, calculate the difference in days from today, and print out a message to the user with this information.



### Solution
```
import datetime

def print_header():
    print("-------------------------------")
    print("    Birthday Countdown App")
    print("-------------------------------")
    print()

def get_birthday_from_user():
    # Get birthday details from the user and return a date object
    year = int(input("Enter your birth year (YYYY): "))
    month = int(input("Enter your birth month (MM): "))
    day = int(input("Enter your birth day (DD): "))
    return datetime.date(year, month, day)

def compute_days_between_dates(original_date, target_date):
    # Compute the difference in days between two dates
    this_year_birthday = datetime.date(target_date.year, original_date.month, original_date.day)
    delta = this_year_birthday - target_date
    return delta.days

def print_birthday_information(days):
    # Print information about the days until/since birthday
    if days < 0:
        print(f"Your birthday occurred {abs(days)} days ago this year.")
    elif days > 0:
        print(f"Your birthday is in {days} days.")
    else:
        print("Happy birthday!!!")

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    days_until_birthday = compute_days_between_dates(bday, today)
    print_birthday_information(days_until_birthday)

if __name__ == "__main__":
    main()
```
