import os
import sys

n = len(sys.argv)
flag = sys.argv[1]

print("# Set "+flag) 

def convert(str):

	tokens = str.split('-')
	reqd = ' '.join(tokens)
	reqd = reqd.title()
	print("- [ ] **{problemName}**".format(problemName = reqd))
	print("    - [ ] Solution")
	print("    - [ ] Test Cases")
	print("    - [ ] Testing")
	print("    - [ ] Editorial")

dirs = list(filter(os.path.isdir, os.listdir(".")))
dirs.sort()

for item in dirs:
	convert(item)

print()
print('---')