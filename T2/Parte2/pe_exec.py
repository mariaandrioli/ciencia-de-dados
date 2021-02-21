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

def isExecutable(section):
    characteristics = getattr(section, 'Characteristics')
    if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
        return True
    return False

def main(filename):
	all_execs = {}
	execs = []
	if filename.endswith(".exe"):
		pe = pefile.PE(filename)
		for section in pe.sections:
			if isExecutable(section):
				execs.append(section.Name.decode('utf-8').rstrip('\x00'))
	all_execs[filename] = execs

	print(all_execs)

if __name__ == "__main__":
	filename = sys.argv[1]
	main(filename = filename)