#Validating credit cards using Luhn's algorithm
#https://www.youtube.com/watch?v=wsphC8V36i0

ccn = str(input("Enter a credit card number to validate (Mastercard, Visa, Discover, Amex only): "))


def validate_cc(number):
    ccn_reverse = number[::-1]  #[start:stop:step] is how you slice in python, with -1 we're reversing order.
    total = 0
    for i in ccn_reverse[1::2]: #starting from index 1 till end with a step of two, i.e only even numbers
        x = int(i) * 2
        if len(str(x)) == 2:    #If x =9*2 = 18, total = total=(1+8), so we convert number to str first
            for digit in str(x):
                total += int(digit) #https://kite.com/python/answers/how-to-sum-the-digits-of-a-number-in-python
        else:
            total += int(x)

    for i in ccn_reverse[::2]:  #All odd numbers to be added
        total += int(i)

    return total



if validate_cc(ccn) % 10 == 0:
    print("It is a valid credit card number")
else:
    print("It is NOT a valid credit card number")
