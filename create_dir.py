import os

os.system("ls -d */ > temp.txt")
f = open("temp.txt","r").read().split('/\n')[:-1]
for i in f:
	os.system("mv " + i + " " + i.zfill(4)) # It will send error if it is already in the correct spot, but it doesn't damage anything

os.system("ls -d */")