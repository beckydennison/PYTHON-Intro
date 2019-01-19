#wind-chill temp
#twc =35.74 + 0.6215(ta) -35.75v^0.16 +0.4275(ta)v^0.16

def temp_with_windchill():
    ta = eval(input("Enter a temperature in Fahrenheit between -58 and 41:"))
    v = eval(input("Enter a windspeed greater than 2mph:"))
    twc = 35.74 + (0.6215*ta) - (35.75*(v**0.16)) + 0.4275 * ta *(v**0.16)
    print("The wind chill index is", round(twc,5))

temp_with_windchill()

