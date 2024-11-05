def is_spy_number(number):
    digits=[int(digit) for digit in str(number)]
    digit_sum=sum(digits)
    digit_product=1
    for digit in digits:
        digit_product*=digit
    if digit_sum==digit_product:
        return True
    else:
        return False
    
number=int(input())
if is_spy_number(number):
    print('Spy Number')
else:
    print('Not Spy Number')