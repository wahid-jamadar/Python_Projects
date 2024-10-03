# Python Code to Display Calendar of the month of ur choice.

import calendar  
# Enter the month and year.
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar.
print(calendar.month(yy,mm))