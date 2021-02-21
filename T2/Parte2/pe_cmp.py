from xml.etree import ElementTree as et
from xml.dom.minidom import parseString
from itertools import chain
import sys
import os
import json
import pefile

# exemplos diretorios "C:\Program Files\Spark AR Studio\v104\ARStudioWindows.exe"
# "C:\Program Files (x86)\Steam\steam.exe"
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


# * 0x00000020 = Section contains code
# * 0x20000000 = Section is executable

def common_sections(sections):
	values = list(sections.values())
	result = set(values[0]).intersection(*values[1:])
	return result

def unique_sections(sections):
	keys = list(sections.keys())
	values = list(sections.values())
	uniques_dict = {}

	for A in values:
		# Combine all the lists into one
		super_list = list(chain(*values))
		# Remove the items from the list under consideration
		for x in A:
			super_list.remove(x)
		# Get the unique items remaining in the combined list
		super_set = set(super_list)
		# Compute the unique items in this list and print them
		uniques = set(A) - super_set
		uniques_dict[keys.pop(0)] = sorted(uniques)

	return uniques_dict

def get_section(filename):
	result = []
	pe = pefile.PE(filename)
	for section in pe.sections:
		result.append(section.Name.decode('utf-8').rstrip('\x00'))
	return result

def print_all(common, unique):
	print("===================\n\nSecoes comuns\n\n===================\n\n")
	print(common)

	print("\n\n===================\n\nSecoes unicas\n\n===================\n\n")
	print(unique)

def main(files):
	all_execs = {}

	for file in files:
		if file.endswith(".exe"):
			all_execs[file] = get_section(file)

	common = common_sections(all_execs)
	unique = unique_sections(all_execs)

	print_all(common, unique)

if __name__ == "__main__":
	files = [sys.argv[1], sys.argv[2]]
	main(files)