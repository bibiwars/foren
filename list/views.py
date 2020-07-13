from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Case
from analysis.script import analyse
from disk.script import disk_analyse
from network.script import network_analyse
import hashlib
from functools import partial
import os


def list(request):
	print (request)
	if not request.user.is_authenticated:
		return render(request, 'list/login.html')
	else:
		cases = Case.objects.filter(c_owner=request.user)
		return render(request, 'list/index.html', {'cases':cases})


def ready(request, id):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	else:
		case = Case.objects.get(pk=id)
		url = ''
		if not case.c_owner == request.user:
			url = 'analysis:err'
		elif case.c_type == 'memory':
			url = 'analysis:memory'
		elif case.c_type == 'disk':
			url = 'disk:disk'
		elif case.c_type == 'network':
			url = 'network:network'
		else:
			url = 'analysis:err'
		response = redirect(url)
		response.set_cookie('CID', case.c_fingerprint, max_age=900)
		return response


def add_case(request):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	else:
		if request.method == 'POST':
			c_name = request.POST['name'].replace(" ", "_")
			c_type = request.POST['type']
			c_owner = request.user
			##changing filename
			uploaded_file = request.FILES['file']
			fs = FileSystemStorage()
			f = fs.save('uploads/'+c_owner.username+'_'+c_name, uploaded_file)
			c_file = fs.url(f)
			##fingerprint
			with open(c_file, mode='rb') as f:
				d = hashlib.md5()
				for buf in iter(partial(f.read, 128), b''):
					d.update(buf)
			c_fingerprint = d.hexdigest()
			
			case = Case(c_name=c_name, c_type=c_type, c_file=c_file, c_fingerprint=c_fingerprint, c_owner=c_owner)
			case.save()

			if case.c_type == 'memory':
				#get selected plugins to run
				#selected_plugs=['envars', 'pslist', 'netscan', 'filescan', 'iehistory', 'chromehistory', 'firefoxhistory', 'cmdscan','screenshot', 'malfind', 'hashdump']
				#script calling
				analyse(c_name, c_type, c_file, c_owner.username)
				#//end//#
			elif case.c_type == 'disk':
				disk_analyse(c_name, c_type, c_file, c_owner.username)
			elif case.c_type == 'network':
				network_analyse(c_name, c_type, c_file, c_owner.username)

		return redirect('list:list')


def delete_case(request, id):
	if not request.user.is_authenticated:
		return render(request, 'list/login.html')
	else:
		case = Case.objects.get(pk=id)
		if case.c_owner == request.user:
			os.popen('rm ' + str(case.c_file))
			case.delete()
		return redirect('list:list')


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				cases = Case.objects.filter(c_owner=request.user)
				return render(request, 'list/index.html', {'cases':cases})
			else:
				return redirect('list:login_user')
		else:
			return redirect('list:login_user')
	else:
		if request.user.is_authenticated:
			cases = Case.objects.filter(c_owner=request.user)
			return render(request, 'list/index.html', {'cases':cases})
		else:
			return render(request, 'list/login.html')


def logout_user(request):
	logout(request)
	return redirect('list:login_user')
