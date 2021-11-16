__author__ = 'guinnc'

class Car:
    def __init__(self, Make, Model, Year, MPG):
        self.make = Make
        self.model = Model
        self.year = Year
        self.mpg = MPG

    def __str__(self):
        return self.make + '\t' + self.model + '\t' + self.year + '\t' +self.mpg

