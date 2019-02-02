#Square root

def sqrt(n):
    threshold = .0001
    nextGuess = n/2
    lastGuess = nextGuess + (2*threshold)
    while abs(lastGuess-nextGuess)>threshold:
        lastGuess = nextGuess
        nextGuess = (nextGuess+n/nextGuess)/2
        square_root = nextGuess
    return square_root
test= sqrt(144)
print(test)

     






