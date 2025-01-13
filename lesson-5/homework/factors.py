n = int(input('Enter a positive integer: '))
def factors():
    i = 0
    while i < n:
        i += 1
        if n%i == 0: 
            print(i, 'is a factor of ', n)
        else:  
            pass
factors()