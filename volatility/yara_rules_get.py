#!/usr/bin/env python
# encoding: utf-8

import os
import shutil

def get_rules_from_git():
	shutil.rmtree("./rules")
	os.system("git clone https://github.com/Yara-Rules/rules.git")

def list_yara_files():
	all_yara_files = []
	for root, directories, filenames in os.walk("./rules/malware"):
		print ("Processing " + root)
		filenames.sort()
		for file_name in filenames:
			rule_filename, rule_file_extension = os.path.splitext(file_name)
			if rule_file_extension == ".yar" or rule_file_extension == ".yara":
				all_yara_files.append(os.path.join(root, file_name))
	return all_yara_files

def remove_incompatible_imports(files):
	filtered_files = []
	for yara_file in files:
		with open(yara_file, 'r') as fd:
			yara_in_file = fd.read()
			if not (("import \"math\"" in yara_in_file) or ("import \"cuckoo\"" in yara_in_file) or ("import \"hash\"" in yara_in_file) or ("imphash" in yara_in_file)):
				filtered_files.append(yara_file)
	return filtered_files

def fix_duplicated_rules(files):
	filtered_files = []
	first_elf = True
	to_delete = False
	for yara_file in files:
		print ("Processing " + yara_file)
		with open(yara_file, 'r') as fd:
			yara_in_file = fd.readlines()
			for line in yara_in_file:
				if line.strip() == "private rule is__elf {":
					if first_elf:
						first_elf = False
					else:
						to_delete = True
				if not to_delete:
					filtered_files.append(line)
				if (not first_elf) and line.strip() == "}":
					to_delete = False
			filtered_files.append("\n")
	return filtered_files

def merge_rules(all_rules):
	with open("malware_rules.yar", 'w') as fd:
		fd.write(''.join(all_rules))

def main():
	get_rules_from_git()
	all_yara_files = list_yara_files()
	all_yara_filtered_1 = remove_incompatible_imports(all_yara_files)
	all_yara_filtered_2 = fix_duplicated_rules(all_yara_filtered_1)
	merge_rules(all_yara_filtered_2)

# Main body
if __name__ == '__main__':
	main()
