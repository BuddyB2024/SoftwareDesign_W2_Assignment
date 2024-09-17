# this is an application that is used to perform operations on fractions
# it is a class that is used to create fractions and perform operations on them
# it has the following methods:
# __init__ : this is the constructor of the class, it is used to create a fraction object
# __str__ : this is a method that is used to return the string representation of the fraction
# __add__ : this is a method that is used to add two fractions
# __sub__ : this is a method that is used to subtract two fractions
# __mul__ : this is a method that is used to multiply two fractions
# __truediv__ : this is a method that is used to divide two fractions

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        if den < 0:
            num = -num
            den = -den
        elif den == 0:
            raise ZeroDivisionError("division by zero")
        return Fraction(num, den)
    
# creating two fractions
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print("Debug: Running the latest version of fraction_class.py")  # Add this at the top of your script

# adding two fractions
f3 = f1 + f2
print(f"Addition of {f1} and {f2} is {f3}") # output: Addition of 1/2 and 1/3 is 5/6

# subtracting two fractions
f4 = f1 - f2
print(f"Subtraction of {f1} and {f2} is {f4}") # output: Subtraction of 1/2 and 1/3 is 1/6

# multiplying two fractions
f5 = f1 * f2
print(f"Multiplication of {f1} and {f2} is {f5}") # output: Multiplication of 1/2 and 1/3 is 1/6

# dividing two fractions
f6 = f1 / f2
print(f"Division of {f1} and {f2} is {f6}") # output: Division of 1/2 and 1/3 is 3/2
print(f6) # output: 3/2

# dividing by zero
f7 = Fraction(1, 0)
print(f7) # output: division by zero
