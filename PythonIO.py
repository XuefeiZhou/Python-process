import os
ls = os.linesep

#get filename
while True:
    fname = raw_input('create a file:')
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

#get file content(text) lines

content = []
print"\nEnter lines ('quit' by itself to quit)\n"

#loop until user terminates input
while True:
    entry = raw_input('>>')
    if entry == 'quit':
        break
    else:
        content.append(entry)

#write lines to file with proper line-ending

myfile = open(fname,'w')
myfile.writelines('%s%s' % (x, ls) for x in content)
myfile.close()
print "Done!"

