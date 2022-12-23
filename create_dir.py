import os

os.system("ls -d */ > temp.txt")
f = open("temp.txt","r").read().split('/\n')[:-1]
m = max([len(x) for x in f]) # Get the largest length of problem number solved (ie. if we have [1,2,20,1000] -> 4)

for i in f:
	os.system("mv " + i + " " + i.zfill(m)) # It will send error if it is already in the correct spot, but it doesn't damage anything

os.system("ls -d */")