#!/usr/bin/python

#
# A script to count the number of lines, words, numbers, chars
# and double words in a UTF 8 text file.
#

import re,sys

def main():
	(line_counter,word_counter,char_counter,num_counter,double_word_counter)=(0,0,0,0,0)

	# Open text file for reading
	try:
		text_file_name = raw_input("Enter file name: ")
		text_file = open(text_file_name,"r")
	except IOError:
		print "Could not open file %s for reading" % text_file_name
		sys.exit()

	# Update counters
	for line in text_file.readlines():
		line_counter+=1
		char_counter+=len(re.findall(r'.',line,re.S))
		word_counter+=len(re.findall(r'\S+(\s+|$)',line))
		num_counter+=len(re.findall(r'\s+\d+\s+',line))
		double_word_counter+=len(re.findall(r'\b(\w+)\s+\1\b',line))
		
	# Print summary
	print "\n------------------------------------\n"
	print "Number of characters found in text\t:%d" % char_counter
	print "Number of lines found in text\t:%d" % line_counter
	print "Number of words found in text\t:%d" % word_counter
	print "Number of numbers found in text\t:%d" % num_counter
	print "Number of duplicated words found\t:%d" % double_word_counter
	
main()