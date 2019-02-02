# Pentagonal_Number 

def getPentagonalNumber(n):
    p = ((n*((3*n)-1)))/ 2
    return(p)


for i in range (1, 101):
    print((int(getPentagonalNumber(i))), end= " ")
    if i % 10 == 0:
        print()
    
