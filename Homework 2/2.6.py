#sum dighits in an integer

def sumOfDigits():

    n=int(input("Enter integer beteween 0 and 1000:")) 
    sum=0
    while n!=0 :

        m=n%10
        n=n/10
        sum=int(sum+m)

    print(sum)

sumOfDigits()
