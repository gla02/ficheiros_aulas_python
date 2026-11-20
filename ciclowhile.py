prime = True
number = 2
while prime:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    print(f"{number} is prime: {prime}")
    number += 1
