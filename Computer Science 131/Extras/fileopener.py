#First Name, MI LastName president and  term length

presFile = open('President.txt','r')

line = presFile.readline()
empty_string = ""
while line != empty_string:
    comma_idx = line.find(',')
    para_idx = line.find('(')
    hyph_idx = line.find('-')

    fn = line[comma_idx + 2: para_idx]
    ln = line[: comma_idx]
    sYear = line[para_idx + 1: para_idx + 5]
    eYear = line[para_idx + 6: para_idx + 10]
    if eYear != '':
        EYear = ' to ' + eYear
    else:
        EYear = ''
    print(fn + ln ,'was President from', sYear + EYear)
    
    line = presFile.readline()
