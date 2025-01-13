def prime(n):
    i = 1
    a = 0
    while i <= n:
        if n % i == 0:
            a += 1
        else:
            pass
        i += 1
    if a == 2:
        print('True')
    else: 
        print('False')
prime(12)