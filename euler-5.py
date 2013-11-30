# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Using 2520 as the count incrementer and not checking redundant factors (e.g. 1-10) saves a bunch of time.


count = 2520
factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while True:
    for factor in factors:
        if count % factor != 0:
            break
        elif factor == 20:
            print(count)
            exit()
    count += 2520

