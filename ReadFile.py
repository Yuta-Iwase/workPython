name = "test.ipynb"
#readFile = open(name,"r")
#
#
#print readFile.readline()
##print readFile.readline()
##print readFile.readline()
##print readFile.readline()
#
##print readFile.next()
#print readFile.next() in readFile


infile = open(name, "r")  # Open file for reading
line = infile.readline()      # Read first line
# Read x and y coordinates from the file and store in lists
x = []
y = []
a=0
for line in infile:
#    print line
    print (line in infile)
    print (a)
    a=a+1
infile.close()
