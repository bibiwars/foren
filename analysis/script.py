#!/usr/bin/env python

import os
import subprocess
import json
import time
from threading import Thread
from . import lab_settings
from list.models import Case


def pid_dump(filename, profile_name, p):
	path = os.path.join('analysis', 'templates', 'analysis', 'memory') + '/'
	process = subprocess.Popen([lab_settings.python_path, lab_settings.vol_path, '-f', str(filename), '--profile='+profile_name, 'procdump', '-D', 'files', '-p', p],
							   stdout=open(path + 'proc_dump_log', 'w+'))
	process.wait()
	return 0


def f_dump(filename, profile_name, Q):
	path = os.path.join('analysis', 'templates', 'analysis', 'memory') + '/'
	Q = hex(int(Q))
	print(Q)
	process = subprocess.Popen([lab_settings.python_path, lab_settings.vol_path, '-f', str(filename), '--profile='+profile_name, 'dumpfiles', '-D', 'files', '-Q', Q, '-n'],
							   stdout=open(path + 'file_dump_log', 'w+'))
	process.wait()
	return 0


## initials: folders creation + profile search
def scan_init(filename, c_owner, c_name):
	os.system('mkdir -p ' + path + c_owner+'_'+c_name+'_screenshots')
	time.sleep(0.5)
	process = subprocess.Popen( [lab_settings.python_path, lab_settings.vol_path, '-f', filename, 'imageinfo',
	 '--output-file=' + path + c_owner+'_'+c_name+'_init.json', '--output=json'] ,stdout=open(path + 'init_log', 'w+'))
	process.wait()
	return 0


## running a plugin
def run_plugin(filename, profile_name, command, output, output_file, more_options):
	print ("+++Launching " + command)
	process = subprocess.Popen( [lab_settings.python_path, lab_settings.vol_path, '-f', filename,
	 '--profile=' + profile_name, command, output_file, output, more_options] ,stdout=open(path + command + '_log', 'w+'))
	process.wait()


# running a set of plugins
def run_plugs(selected_plugs, profile_name, c_owner, c_name, c_file):
	for plug in selected_plugs:
		if plug in lab_settings.supported_json_plugins:
			run_plugin(c_file, profile_name, plug, '--output=json', '--output-file=' + path + c_owner+'_'+c_name+'_'+plug+'.json', '')
		elif plug in ['screenshot']:
			run_plugin(c_file, profile_name, plug, '--dump-dir=' + path + c_owner+'_'+c_name+'_screenshots', '', '')
		elif plug in ['yarascan']:
			run_plugin(c_file, profile_name, plug, '--output=json', '--output-file=' + path + c_owner+'_'+c_name+'_'+plug+'.json', '--yara-file=volatility/malware_rules.yar')
		else:
			run_plugin(c_file, profile_name, plug, '', '--output-file=' + path + c_owner+'_'+c_name+'_'+plug+'.txt', '')
	# make case ready
	case = Case.objects.get(c_name=c_name)
	case.c_status = True
	case.save()


def analyse(c_name, c_type, c_file, c_owner):
	
	# Initializing some vars
	global path
	path = os.path.join('analysis', 'templates', 'analysis', c_type) + '/'
	global log_path
	log_path = './full_log'
	
	# check if file exists
	if os.path.isfile(c_file):
		# make dirs, and find profile
		scan_init(c_file, c_owner, c_name)
		with open(path + c_owner+'_'+c_name+'_init.json') as init:
			data = json.load(init)
			profile_name = (str(data['rows'][0][0]).split(','))[0]
		# check if case type unsupported
		if 'No suggestion' in profile_name:
			case = Case.objects.get(c_name=c_name)
			case.c_unsupported=True
			case.save()
		else:
			selected_plugs = lab_settings.supported_plugins
			Thread(target=run_plugs, args=(selected_plugs, profile_name, c_owner, c_name, c_file)).start()
		
	else:
		print ("File not found")
		print (c_file)
		exit(0)
