lc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
up = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ')
morseCode = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",' ')
#Library for All Possible Letters
sentence = str(input("What is the sentence that needs to be converted? "))

lcLength = len(lc)
sentenceLength = len(sentence)
start = 0

while start < sentenceLength: #Start is the first letter through last letter of the sentence
    n = 0
    while n < lcLength: #Tests each letter to see if it matches to either lc or up
        if sentence[start] == lc[n]:
            print(morseCode[n])
            n = lcLength - 1
        if sentence[start] == up[n]:
            print(morseCode[n])
            n = lcLength
        n += 1
    start += 1
