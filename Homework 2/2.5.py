#Tip

subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate separated by a comma:"))
tip =(gratuity/100)*subtotal
total = tip + subtotal
print("The gratuity is", (round(tip, 2)), "and the total is", round(total, 2))
