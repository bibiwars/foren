from threading import Thread
from list.models import Case
import subprocess
import os


def DISKtype(c_file):
	return os.popen('file ' + c_file).read()


def run_DISKplugs(c_owner, c_name, c_file):
	# binwalk
	process = subprocess.Popen(['binwalk', c_file], stdout=open(path + c_owner + '_' + c_name + '_binwalk.txt', 'w+'))
	process.wait()
	# make case ready
	case = Case.objects.get(c_name=c_name)
	case.c_status = True
	case.save()


def disk_analyse(c_name, c_type, c_file, c_owner):
	global path
	path = os.path.join('disk', 'templates', 'disk') + '/'

	# check if file exists
	if os.path.isfile(c_file):
		# check if case type unsupported
		file_type = DISKtype(c_file)
		if not 'Disk' in file_type:
			case = Case.objects.get(c_name=c_name)
			case.c_unsupported = True
			case.save()
		else:
			Thread(target=run_DISKplugs, args=(c_owner, c_name, c_file)).start()

	else:
		print("File not found")
		print(c_file)
		exit(0)
