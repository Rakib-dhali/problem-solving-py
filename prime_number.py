# Rakib Dhali
# pyrhon programme to check if a number is prime or not

number = int(input("Enter the number: "))

if number <= 1:
    print("No, the number isn't a Prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("No, the number isn't a Prime number.")
            break
    else:
        print("Yes, the number is a Prime number.")
