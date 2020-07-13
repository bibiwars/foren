from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import *
from list.models import Case
import os
from django.contrib import admin
from django.contrib.admin.models import LogEntry


def index(request):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	case_n = Case.objects.count()
	user_n = User.objects.count()
	disk_usage = os.popen('du -hc . | tail -1 |tr "\t" " "|cut -d " " -f1').read
	print("_______")
	log = LogEntry.objects.all()
	log_table = []
	action_flag = 'Added'
	for l in log:
		if str(l.action_flag) == '1':
			action_flag = 'Added'
		if str(l.action_flag)== '2':
			action_flag = 'Changed'
		if str(l.action_flag)== '3':
			action_flag = 'Deleted'
		log_table.append([str(l.user), action_flag, str(l.object_repr), str(l.action_time)])
	return render(request, 'manager/index.html', {'case_n':case_n,'user_n':user_n,'disk_usage':disk_usage,'logs':log_table})


def users(request):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	users = User.objects.all()
	return render(request, 'manager/users.html', {'users':users})


def user_add(request):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	##add the user
	if request.method == 'POST':
		User.objects.create_user(username=request.POST['username'].replace(" ", "_"), email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'])
	return redirect('manager:users')


def user_remove(request, user):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	##remove the user
	u = User.objects.get(username=user)
	u.delete()
	return redirect('manager:users')


def user_ch(request, user):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	cuser = User.objects.get(username=user)
	return render(request, 'manager/user_ch.html', {'user':cuser})


def user_ch_gen(request, user):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	##change the data
	u = User.objects.get(username = user)
	u.email = request.POST['email']
	u.first_name = request.POST['first_name']
	u.last_name = request.POST['last_name']
	if request.POST['admin']=='0':
		u.is_superuser = False
	else:
		u.is_superuser = True
	u.save()
	return redirect('manager:users')


def user_ch_pwd(request, user):
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not request.user.is_superuser:
		return redirect('list:login_user')
	##change the password
	u = User.objects.get(username = user)
	if u.check_password(request.POST['old']):
		if request.POST['new']==request.POST['new_re']:
			u.set_password(request.POST['new'])
			u.save()
			return redirect('manager:users')
		return render(request, 'manager/user_ch.html', {'user':u,'err':'An error has occured'})
	return render(request, 'manager/user_ch.html', {'user':u,'err':'An error has occured'})


def groups(request):
	return HttpResponse("groups")


def group_ch(request, user):
	return HttpResponse("groups change")


def clears(request):
	os.system('rm uploads/*')
	return redirect('manager:index')
