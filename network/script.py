from threading import Thread
from list.models import Case
import subprocess
from analysis import lab_settings
import os


def NTtype(c_file):
	return os.popen('file ' + c_file).read()


def run_NTplugs(c_owner, c_name, c_file):
	# capinfos
	print("capinfos")
	process = subprocess.Popen(['capinfos', c_file], stdout=open(path + c_owner + '_' + c_name + '_capinfos.txt', 'w+'))
	process.wait()
	# dump files
	print("dump files")
	process = subprocess.Popen(['tcpxtract', '-f', c_file, '-o', 'files'], stdout=open(path+c_owner+'_'+c_name+'_tcpxtract.txt', 'w+'))
	process.wait()
	# scan HTTP with CapTipper
	print("scan HTTP with CapTipper")
	process = subprocess.Popen([lab_settings.python_path, lab_settings.cap_path, '-r', path+'.', c_file], stdout=open(path + c_owner + '_' + c_name + '_captipper.txt', 'w+'))
	process.wait()
	if not os.path.isfile(path + c_owner + '_' + c_name + '_captipper.html'):
		os.popen('touch ' + path + c_owner + '_' + c_name + '_captipper.html')
	# make case ready
	print("ready")
	case = Case.objects.get(c_name=c_name)
	case.c_status = True
	case.save()


def network_analyse(c_name, c_type, c_file, c_owner):
	global path
	path = os.path.join('network', 'templates', 'network') + '/'

	# check if file exists
	if os.path.isfile(c_file):
		# check if case type unsupported
		file_type = NTtype(c_file)
		if not 'tcpdump' in file_type:
			case = Case.objects.get(c_name=c_name)
			case.c_unsupported=True
			case.save()
		else:
			Thread(target=run_NTplugs, args=(c_owner, c_name, c_file)).start()

	else:
		print("File not found")
		print(c_file)
		exit(0)
