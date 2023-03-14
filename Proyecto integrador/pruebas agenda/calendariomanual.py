from tkinter import *
from calendar import monthrange
 
class Application(Frame):
 
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
 
        # Get year and month from user input
        year_input = input('\nEnter Year eg. 2020\n')
        while not year_input.isdigit():
            year_input = input('Please enter a valid year as a positive integer:\n')
        year = int(year_input)
        

        month_input = input('\nEnter month number.\n')
        while not month_input.isdigit() or int(month_input) not in range(1, 13):
            month_input = input('Please enter a valid month as an integer between 1 and 12:\n')
        month = int(month_input)

        # Create widgets for the calendar
        self.create_widgets(year, month)
 
    def create_widgets(self, year, month):
 
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        # Create labels for the days of the week
        for i in range(7):
            label = Label(self, text=days[i])
            label.grid(row = 0, column = i)
 
        weekday, numDays = monthrange(year, month)
        week = 1

        # Create buttons for each day of the month
        for i in range(1, numDays + 1):
            button = Button(self, text = str(i))
            button.grid(row = week, column = weekday)

            # Move to the next row if at the end of the week
            weekday += 1
            if weekday > 6:
                week += 1
                weekday = 0

# Create the application and start the main loop
root=Tk()
obj = Application(root)
root.mainloop()
