import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_dat = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_dat}")

def calculate_future_date():
    number_of_days =int(input("Enter the number of days to add to the current date:"))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days = number_of_days)
    formatted_dat = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_dat}")