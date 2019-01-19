#calc years and days from minutes

def convert_to_d_y(minutes):
   days, minutes = divmod(minutes, 1440)
   years, days = divmod(days, 365)
   print("Year(s):", years, "and", "Day(s):", days)
   
minutes = int(input("Enter number of minutes to convert to days and years:"))

convert_to_d_y(minutes)









