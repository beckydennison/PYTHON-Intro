#calculate energy needed for temp change
#Q = m[weight of water in kg] * (finalTemperature – initialTemperature) * 4184
def calc_joules_temp():
    m = eval(input("Enter the amount of water in kilograms:"))
    itemp = eval(input("Enter the intial temperature:"))
    ftemp = eval(input("Enter the final tempreature:"))
    Q = m*(ftemp - itemp) *4184
    print("The energy needed is", Q, "joules.")

calc_joules_temp()



