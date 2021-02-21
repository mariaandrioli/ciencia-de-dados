from xml.etree import ElementTree as et
from xml.dom.minidom import parseString
from itertools import chain
import sys
import os
import json

def common_permissions(permissions):
	values = list(permissions.values())
	result = set(values[0]).intersection(*values[1:])
	return result

def unique_permissions(permissions):
	keys = list(permissions.keys())
	values = list(permissions.values())
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

def final_print(permissions, common, unique):
	print("===================\n\nPermissoes por APK\n\n===================\n\n")
	print(json.dumps(permissions, indent = 4))

	print("\n\n===================\n\nPermissoes unicas por APKs\n\n===================\n\n")
	print(json.dumps(unique, indent = 4))

	print("\n\n===================\n\nPermissoes comuns das APKs\n\n===================\n\n")
	print(common)

def main(directory):
	all_permissions = {}
	for filename in os.listdir(directory):
		if filename.endswith(".xml"):
			with open(os.path.join(directory, filename),'r') as f:
				data = f.read()
			dom = parseString(data)
			nodes = dom.getElementsByTagName('uses-permission')
			
			permissions = []
			for node in nodes:
				permissions.append(node.getAttribute('android:name').split('.')[-1])
			all_permissions[filename] = permissions
		else:
			continue

	final_print(all_permissions, common_permissions(all_permissions), unique_permissions(all_permissions))

if __name__ == "__main__":
	directory = sys.argv[1]
	main(directory = directory)