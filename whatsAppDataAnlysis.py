import os
import sys

__author__ = 'tusharsaurabh'

home = os.environ['HOME']
source = home + '/Downloads/WhatsApp Chat with The Crazies -3.txt'
destination = home + '/Documents/whatsAppDataAnalysisTodaysChat.txt'
f=open(source,'r')
w=open(destination,'w')

DATE = "11/10/2015"

firstLine = False
read = 0
written = 0
for line in f:
    read = read + 1
    if line[0:10] == '11/10/2015' or firstLine:
        firstLine = True
        written = written + 1
        w.write(line)

print 'read :' + str(read)
print 'written: ' + str(written)

f.close
w.close
