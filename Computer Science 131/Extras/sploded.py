class ExplodedStr(str):
    def __init__(self, value=""):
        str.__init__(value)

    def explode(self):
        if len(self) == 0:
            return self
        else:
            tempStr = ""
            for i in range(len(self) - 1):
                tempStr += self[i] + " "
            tempStr += self[-1]
            return tempStr

regStr = 'The quick brown fox jumps over the lazy dog.'
expStr = ExplodedStr(regStr)
print('regStr:', regStr)
print('expStr:', expStr)
print('Exploded:', expStr.explode())
print('expStr:', expStr)
