import os

temp = 4
while(temp > 0):
	fname = input("Enter text file name: ")
	num_lines = 0
	with open(fname, 'r') as f:
	    for line in f:
	        num_lines += 1
	print("Number of lines:")
	print(num_lines)
	if (num_lines == 0):
		os.remove(fname)
		print("File Removed!")
	elif (num_lines < 10):
		os.rename(fname, 'short_' + fname)
		print("File Renamed!")
	elif (num_lines <= 20):
		os.rename(fname, 'medium_' + fname)
		print("File Renamed!")
	elif (num_lines > 20):
		os.rename(fname, 'long_' + fname)
		print("File Renamed!")
	temp = temp - 1
