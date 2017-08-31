from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "Thge input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit Return to continue, Ctrl_C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

