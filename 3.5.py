def isValid(number):

    validatelist=[] #brackets how define array/get spread of numbers
    evens = 0
    odds = 0
    
    for i in number:
        validatelist.append(int(i))

    def sumOfDoubleEvenPlace(number):
        for i in range(0,len(number),-2):


            validatelist[i] = validatelist[i]*2

            def getDigit(number):

                if validatelist[i] >= 10:

                    validatelist[i] = validatelist[i]//10 + validatelist[i]%10

            evens = evens + validatelist[i]
            print(evens)
   
    def sumOfOddPlace(number):
        for i in range(1,len(number),-2):
            validatelist[i]
            odds = odds + validatelist[i]
            print(odds)
        
    if (odds + evens)%10 == 0:
        print('True')

    else:
        print('This is not valid credit card')

def cardnumber():

    result=''
    while True:
        try:
            result = input('Please enter the 13-16 digit credit card number : ')

            if not (len(result)>=13 and len(result)<= 16) or not type(int(result) == int) :
                raise Exception

        except Exception:    
            print('That is not a proper credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
            continue

        else:
            break


    return result

def goagain():
    return input('Do you want to check again? (Yes/No) : ').lower()[0] == 'y'

def main():

    while True:

        result = cardnumber()
        isValid(result)


        if not goagain():
            break

if __name__ == '__main__':
    main()
