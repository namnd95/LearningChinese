# This converts the Chinese work list 
# to the input format of the Chinese worksheet generator.

import codecs
import sys

from sets import Set

def isSame(line):
    if len(line) <= 1:
        return False
    
    for i in xrange(1, len(line)):
        if line[i] != line[0]:
            return False
            
    return True
    
    
def getWords(line):
    end = len(line)
    for i in xrange(len(line)):
        if line[i] == ' ' or line[i] == '\t':
            end = i
            break

    line = line[:end]
    if isSame(line):
        line = line[:1]
        
    
    if len(line) > 1:
        line = '(' + line + ')'
    return line
        
def convert(input, output):
    with codecs.open(input, 'r', encoding='utf8') as fi:
        with codecs.open(output,'w',encoding='utf8') as fo:
            curLine = ''
            for line in fi: 
                line = line.strip()
                line = getWords(line)
                curLine = curLine + line + ' '
                if len(curLine) > 30:
                    fo.write('%s\n' % curLine)
                    curLine = ''
            fo.write('%s\n' % curLine)

def checkDup(input):
    output = ''
    traditional = ''
    simplified = ''
    with codecs.open(input, 'r', encoding='utf8') as fi:
        s = Set()
        record = False
        for line in fi:
            line = line.strip()
            if line == "":
                record = True
            output = output + line + '\n'
            for c in line:
                if c not in s:
                    if record:
                        simplified = simplified + c
                    else:
                        traditional = traditional + c
                    s.add(c)

    with codecs.open(input, 'w', encoding='utf8') as fo:
        fo.write('%s' % output)
        fo.write('%s\n' % traditional)
        fo.write('%s\n' % simplified)
        
def normalise(input, length):
    output = ''
    last = ''
    with codecs.open(input, 'r', encoding='utf8') as fi:
        for line in fi:
            line = line.strip()
            while len(line) < length:
                line = line + ' '
            output = output + line + '\n'                      
                   
    with codecs.open(input, 'w', encoding='utf8') as fo:
        fo.write('%s' % output)

            
# python convert.py wordlist/coursera-hsk1-peking/week1.txt wordlist/coursera-hsk1-peking/week1-input.txt
if __name__ == "__main__":
    #convert('wordlist/coursera-hsk1-peking/week2.txt', 'wordlist/coursera-hsk1-peking/week2-input.txt')
    #exit(0)
    if sys.argv[1] == 'convert':
        convert(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'check':
        checkDup(sys.argv[2])
    elif sys.argv[1] == 'normalise':
        normalise(sys.argv[2], int(sys.argv[3]))
 
