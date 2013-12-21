#!/usr/bin/python

'''
Write a clone of the tail program available in unix/linux 
systems but only support a very small subset of the 
flags/options/features it supports. Pick and choose the 
complexity/scope based on the time you have and the options 
you like to support. Support at least the basic functionality 
you get with no options.

man tail - http://unixhelp.ed.ac.uk/CGI/man-cgi?tail

@author: Karan Goel
@email: karan@goel.im
'''

import os
import argparse

import time

BUFFER_SIZE = 1024

def get_last_bytes(filename, bytes):
	'''
	Returns the last 'bytes' bytes from the given file.
	'''
	with open(filename) as f:
		file_size = os.stat(filename).st_size
		
		if file_size <= bytes:
			# we have less stuff than we want
			return f.read()
		else:
			f.seek(-bytes, 2) # move to the appropriate position
			return f.read() # read everything after current position


def get_last_lines(filename, num_lines=10, follow=False):
	'''
	Returns the last 10 lines of input file.
	'''
	with open(filename) as f:
		file_size = os.stat(filename).st_size

		f.seek(0, 2) # move to end of file
		lines_to_read = num_lines # number of lines to read, or the number of '\n'
		line_counter = 1 # number of lines we've read, also used to move reading 'cursor'
		lines_data = [] # stores all data read

		while lines_to_read > 0 and file_size > 0:
			# we still need to read more lines here
			if (file_size > BUFFER_SIZE):
				# we can safely read a buffer here
				# move back a BUFFER_SIZE from end
				f.seek(-line_counter * BUFFER_SIZE, 2) 
				# read data from file
				lines_data.append(f.read(BUFFER_SIZE))
			else:
				# not enough content in file
				f.seek(0, 0) # move to start of file
				# read and store what's left
				lines_data.append(f.read(file_size))

			lines_to_read -= lines_data[-1].count('\n') # sleek trick
			file_size -= BUFFER_SIZE # reduce filesize for next iteration
 			line_counter += 1

 		last_lines = ''.join(lines_data).splitlines()[-num_lines:]

		return '\n'.join(last_lines)

def follow(filename):
	'''
	output appended data as the file grows
	'''
	print get_last_lines(filename) # execute 'tail' normally

	with open(filename) as f:
		f.seek(0, 2)
		while True:
			position = f.tell()
			new = f.read()
			if not new:
				f.seek(position)
				time.sleep(1)
			else:
				print new


def main():
	parser = argparse.ArgumentParser(description="output the last part of file")
	
	parser.add_argument("filename", 
		help="The input filename on which we should tail.")

	parser.add_argument("-c", "--bytes", type=int, 
		help="output the last BYTES bytes. BYTES must be a positive integer")
	
	parser.add_argument("-n", "--lines", type=int, default=10,
		help="output the last LINES lines. LINES must be a positive integer")
	
	parser.add_argument("-f", "--follow", default=False, action='store_true', 
		help="Follow the file for changes, and re-execute tail")
	
	args = parser.parse_args()

	filename = args.filename

	if args.bytes:
		print get_last_bytes(filename, args.bytes)
	elif args.follow:
		follow(filename)
	else:
		print get_last_lines(filename, num_lines=args.lines)

if __name__ == '__main__':
	main()