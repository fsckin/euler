# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(object):
    object = str(object)
    if object[::-1] == object:
        return True
    else:
        return False

largest_palindrome=0

for x in range(100, 1000):
    for y in range(100, 1000):
        product=x*y
        if palindrome(product):
            if product >= largest_palindrome:
                largest_palindrome = product

print(str(largest_palindrome))

