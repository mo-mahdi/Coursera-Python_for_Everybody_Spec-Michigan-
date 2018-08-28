'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

#SOLUTION
#------------

fname=input("Enter file name:")
names=list()
counts=dict()
fhandle=open(fname)
for line in fhandle:
    line.rstrip()
    words=line.split()
    if len(words)<2 or words[0] != "From":
        continue
    names.append(words[1])

for name in names:
    counts[name] = counts.get(name,0)+1
largestname=None
largestnamecount=None
for name,count in counts.items():
    if largestnamecount is None or count > largestnamecount:
        largestname=name
        largestnamecount=count
print(largestname, largestnamecount)
