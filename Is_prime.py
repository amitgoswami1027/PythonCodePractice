
# Function to check if the given number is prime or not
def is_prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print("Number is Prime")
    else:
        print("Number is Not Prime")

next = True
while next:
    new_number = int(input("Enter the number"))
    is_prime(new_number)
    n = int(input("Should we continue, type 0 to exit or enter any key to continue"))
    if n == 0:
        next = False

