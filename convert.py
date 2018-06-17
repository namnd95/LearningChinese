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
    last = ''
    with codecs.open(input, 'r', encoding='utf8') as fi:
        s = Set()
        for line in fi:
            line = line.strip()
            output = output + line + '\n'
            for c in line:
                if c not in s:
                    last = last + c
                    s.add(c)

    with codecs.open(input, 'w', encoding='utf8') as fo:
        fo.write('%s' % output)
        fo.write('%s' % last)

    
        

                   
            
            
# python convert.py wordlist/hsk2-words.txt wordlist/hsk2-list.txt
if __name__ == "__main__":
    # convert(wordlist/hsk2-words.txt, wordlist/hsk2-list.txt)
    if sys.argv[1] == 'convert':
        convert(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'check':
        checkDup(sys.argv[2])