class Fraction(object):
    def __init__(self, numerator, denominator):
        """call this as frac1 = Fraction(num,den)
           set instance variables here"""
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        """called automatically when we print(object) """
        return "in str:" + str(self.__numerator) + "/" + str(self.__denominator)
    #if __str__ doesnt exist, the code will default to __repr__
    def __repr__(self):
        """called automatically in shell"""
        return "in repr:" + str(self.__numerator) + "/" + str(self.__denominator)

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, rFraction):
        newN = self.__numerator*rFraction.getDenominator() + \
                rFraction.getNumerator() * self.__denominator
        newD = self.__denominator * rFraction.getDenominator()
        return Fraction(newN, newD)

    def __sub__(self, rFraction):
        return self + -rFraction

    def __mul__(self, rFraction):
        newN = self.__numerator * rFraction.getNumerator()
        newD = self.__denominator * rFraction.getDenominator()
        return Fraction(newN, newD)

    def __eq__(self, rFraction):
        val1 = self.__numerator / self.__denominator
        val2 = rFraction.getNumerator() / rFraction.getDenominator()
        return val1 == val2

    def __neg__(self, rFraction):
        return not (self == rFraction)

    def __lt__(self, rFraction):
        val1 = self.__numerator / self.__denominator
        val2 = rFraction.getNumerator() / rFraction.getDenominator()
        return val1 < val2

    def __gt__(self,rFraction):
        val1 = self.__numerator / self.__denominator
        val2 = rFraction.getNumerator() / rFraction.getDenominator()
        return val1 > val2

    def __le__(self, rFraction):
        return (self == rFraction or self < rFraction)

    def __ge__(self, rFraction):
        return (self == rFraction or self > rFraction)
        
    def getNumerator(self):
        return self.__numerator
    def getDenominator(self):
        return self.__denominator
    def setNumerator(self, newNum):
        self.__numerator = newNum
    def setDenominator(self, newDen):
        self.__denominator = newDen



###Main
frac1 = Fraction(1,4)
frac2 = Fraction(1,2)
print('Not equals:     ', frac1 != frac2)
print('Equals:         ', frac1 == frac2)
print('Less than:      ', frac1 <  frac2)
print('Greater than:   ', frac1 >  frac2)
print('Less or equals: ', frac1 <= frac2)
print('Great or equal: ', frac1 >= frac2)


##print('frac1\'s numerator is:', frac1.getNumerator())
##print('frac2\'s numerator is:', frac2.getDenominator())
##frac2.setDenominator(508)
##print('frac2\'s numerator is:', frac2.getDenominator())
