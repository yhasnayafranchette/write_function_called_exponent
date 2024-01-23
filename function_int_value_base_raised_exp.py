# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

#Check if exp is a non-negative integer
def exponent (base,exp):
    if type(exp) == int and exp >=0:
        result = 1

#Loop to calculate base raised to exp
        for number in range(exp):
            result *= base
        return result
    
#Print error message if exp is not a non-negative integer
    else:
        print("Error: exp must be a non-negative integer.")

#Print the result
base_value = 2
exponent_value = 3
result = exponent(base_value, exponent_value)
print(f"{base_value} raised to the power of {exponent_value} is: {result}")
