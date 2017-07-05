# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here

class Hand(object):

    def __init__(self, filename):

        if filename[-4:] != ".txt":
            raise ValueError("This is not a valid file name.")
        self.name = filename
        file = open(filename, 'r')
        cards = []
        newlines = []
        lines = file.readlines()
        for line in lines:
            newlines.append(line.replace("\n",""))
        for line in newlines:
            if line not in cards:
                cards.append(line)
        for card in cards:
            if len(card) != 4:
                raise ValueError("There is a 'card' with invalid number of attributes.")
            for c in card:
                if int(c) < 0 or int(c)>2:
                    raise ValueError("There is a 'card' with invalid attributes.")
        if len(cards) != 12:
            raise ValueError("There are not exactly 12 cards.")
        self.cards = cards
        file.close()

    def setcount(self):
        count = 0
        def validset(card1, card2, card3):
            checks = []
            for i in range(4):
                if (card1[i] == card2[i] and card1[i] == card3[i]) or (int(card1[i]) + int(card2[i]) + int(card3[i]) == 3):
                    checks.append(True)
            if checks == [True, True, True, True]:
                return True
            else:
                return False

        for i in range(10):
            for j in range(i+1, 11):
                for k in range(j+1,12):
                    if validset(self.cards[i], self.cards[j], self.cards[k]):
                        count += 1
        return count
