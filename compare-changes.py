import csv
import sys
import os

def main(argv):
	file_list = []
	for file in os.listdir(os.getcwd()):
		if file.endswith(".tsv"):
			file_list.append(file)

	tsvin1 = csv.reader(open(file_list[len(file_list) - 2],'rb'), delimiter='\t') # old
	tsvin2 = csv.reader(open(file_list[len(file_list) - 1],'rb'), delimiter='\t') # new
	
	list1 = []
	list2 = []
	
	for row1 in tsvin1:
		name1 = row1[1]
		size1 = int(row1[0])
		list1.append((name1, size1))
	
	for row2 in tsvin2:
		name2 = row2[1]
		size2 = int(row2[0])
		list2.append((name2, size2))
		
	output_size = []
	output_name = []
	for (name1, size1) in list1:
		for (name2, size2) in list2:
			if name1 == name2:
				size_change = size2 - size1
				if size_change != 0:
					# print "%d	%s" % (size_change, name1)
					output_size.append(size_change)
					output_name.append(name1)

	for (name2, size2) in list2:
		if not (name2, size2) in list1:
			if not name2 in output_name:
				output_size.append(size2)
				output_name.append(name2)
	
	total_size_growed = 0

	for (i, num) in sorted(enumerate(output_size), key = lambda x:x[1], reverse = True):
		if not is_substring(output_name[i], output_name):
			if output_size[i] > 0:
				print "%s%d	%s" % ("+", output_size[i], output_name[i])
			else:
				print "%d	%s" % (output_size[i], output_name[i])
			total_size_growed += output_size[i]

	print "\n\n-----------------------------"
	if total_size_growed > 0:
		print "Total size increased: %d" % total_size_growed
	else:
		print "Total size decreased: %d" % -total_size_growed
	print "-----------------------------"

def is_substring(s, str_list):
	for sp in str_list:
		if (s in sp) and (s != sp):
			return True
	return False

if __name__ == "__main__":
   main(sys.argv[1:])
