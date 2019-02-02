#Reverse integer

number=int(input("Enter number to be reversed:"))

def reverse(number):
    r = 0
    while (number > 0):
        lastdigit = number % 10
        #print(number)
        r=(r*10) + lastdigit
        #print(lastdigit)
        number = number //10
    return(r)

def palindrome(number):
    if number == reverse(number):
        return(True)
    else:
        return(False)

"""def palindrome(number):
    if str(number)[::-1] == str(number):
        return True
    else:
        return False"""

'''def palindrome(number):
    if number[::-1] == number:
       return True
    else:
       return False'''

print(reverse(number))
print(palindrome(number))



   

   
