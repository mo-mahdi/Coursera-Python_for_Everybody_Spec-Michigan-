'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

#SOLUTION
#--------------


fname=input("Enter file name: ")
fhand=open(fname)
counts=dict()
hours=list()
for line in fhand:
    line.rstrip()
    if len(line)<2 or not line.startswith("From"):
        continue

    pos=line.find(":")
    if line[pos-1] != "m":
        hour=line[pos-2:pos]
        hours.append(hour)

for hour in hours:
    counts[hour]=counts.get(hour,0) +1

lst=list()
for k,v in counts.items():
    newtup=(k,v)
    lst.append(newtup)

lst=sorted(lst)
for k,v in lst:
    print(k,v)
