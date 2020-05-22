#Finding e to nth decimal place using Brothers' formula

import decimal

def Find_Factorial(n):
    factorial = [1]    #We basically specified: Factorial(0) = 1 here.
    for i in range(1, n+1):
        factorial.append(factorial[i-1]*i)    #We're using square brackets because in final brothers formula e is a summation of entire series from n=0 to n
    return factorial

def compute_e(n):
    decimal.getcontext().prec = n+1
    #specifying we want n+1 decimal places
    #We are using decimal type for more accuracy, float doesn't give accuracy
    #n+1 because it prec = 1 will be like 8.0, whereas prec=2 will be 8.70 and prec = 3 is like 8.710
    e=2
    factorial = Find_Factorial(2*n + 1)
    for i in range(1,n+1):
        numerator = 2*i + 2
        denominator = factorial[2*i + 1] #Very imp to remember it is a list in denom
        #In above line we used factorial as it will be an int(single number value), if we use Find_Factorial
        #that gives us a list, and can't be added to e which is a number
        e += decimal.Decimal(numerator/denominator)
    return e

while True:
    n = int(input(" Enter a number between 1 and 2000")) #Had to take int here otherwise won't compare with <>=
    if n<=0 or n>=2000:
        print("Invalid number")
    elif n >= 0 and n <= 2000:
        break #Introduced break as otherwise loop was continually asking to enter a number

print(str(compute_e(n))[:n + 1])


#Had to take str, as :n + 1 can't work with int
#This last print statement says print the last term of list, ie in list of all summations.
#Try with entering number 3, ans is 2.71. It proves that when you enter decimal places 3, you get 2.71
#When you put decimal places 4 you get 2.718
