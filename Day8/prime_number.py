def prime_checker(number):
    prime_status = True
    for n in range(2, number):
        if number % n == 0:
            prime_status = False
    if prime_status == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)
