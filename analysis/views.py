from django.shortcuts import render, redirect, get_object_or_404
from list.models import Case
import json
import os
from . import script
import subprocess


def get_list_data(case, plug):
	json_data=open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+plug+'.json')
	return json.load(json_data)


def memory(request):
	# TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	# end test cases#
	# get data
	list_data = get_list_data(case, 'init')
	new_list = [[list_data['rows'][i][j] for j in range(len(list_data['rows'][i]))] for i in range(len(list_data['rows']))]
	profile_name = (str(list_data['rows'][0][0]).split(','))[0]
	# return
	detection = []
	# detect1 : malware
	list_malware = get_list_data(case, 'yarascan')
	list_malware = list(dict.fromkeys([item[0] for item in list_malware['rows']]))
	# end detect1
	# detect2 : IPs ----- change it into the script
	list_ips = get_list_data(case, 'netscan')
	list_ips = list(dict.fromkeys([item[3].split(':')[0] for item in list_ips['rows'] if len(item[3].split(':')[0])>0]))
	list2_ips = []
	for ip in list_ips:
		if ip != '0.0.0.0':
			cmd = os.popen('curl -s -G https://api.abuseipdb.com/api/v2/check   --data-urlencode "ipAddress='+ ip +'"   -d maxAgeInDays=90   -d verbose   -H "Key: 24d3a4c5d7a8044396c1075a39d9ec68336c8ff14897087b06f4f147d3d8a69e7acee7e1d4d64a66"   -H "Accept: application/json"').read()
			if not 'errors' in cmd:
				cmd = json.loads(cmd)
				if cmd['data']['abuseConfidenceScore'] >0:
					list2_ips.append([cmd['data']['ipAddress'], cmd['data']['isPublic'], cmd['data']['abuseConfidenceScore']])
	# end detect2
	# detect3 : keyloggerd
	list_ps = get_list_data(case, 'pslist')
	keylog = ['rvlkl.exe', 'keylogger.exe']
	list_ps = list(dict.fromkeys([item[1] for item in list_ps['rows'] if (item[1] in keylog)]))
	# end detect3
	return render(request, 'analysis/sys.html', {'case': case, 'profile':profile_name, 'cpu':new_list[0][6], 'date':new_list[0][len(new_list[0])-1], 'malware':list_malware,'ips':list2_ips,'keylog':list_ps})

def env(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'envars')
	#return
	return render(request, 'analysis/env.html', {'case':case,'env_list':list_data['rows']})

def proc1(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'pslist')
	return render(request, 'analysis/proc1.html', {'case':case,'ps_list':list_data['rows']})

def proc2(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+'pstree'+'.txt').read()
	#return
	return render(request, 'analysis/proc2.html', {'case':case,'tree_list':list_data})

def proc3(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'autoruns')
	#return
	return render(request, 'analysis/proc3.html', {'case':case,'list':list_data['rows']})

def net(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'netscan')
	#return
	return render(request, 'analysis/net.html', {'case':case,'net_list':list_data['rows']})

def files(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'filescan')
	#return
	return render(request, 'analysis/filescan.html', {'case':case,'file_list':list_data['rows']})

def browser1(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+'iehistory'+'.txt').read()
	#return
	return render(request, 'analysis/browser1.html', {'case':case,'browse_list':list_data})

def browser2(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+'chromehistory'+'.txt').read()
	#return
	return render(request, 'analysis/browser2.html', {'case':case,'browse_list':list_data})

def browser3(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+'firefoxhistory'+'.txt').read()
	#return
	return render(request, 'analysis/browser3.html', {'case':case,'browse_list':list_data})

def cmd(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'cmdscan')
	new_list = [[list_data['rows'][i][j] for j in range(len(list_data['rows'][i])) if j not in [4,5,6,7,8,9] ] for i in range(len(list_data['rows']))]
	#return
	return render(request, 'analysis/cmdscan.html', {'case':case,'cmd_list':new_list})

def cmd2(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'cmdline')
	#return
	return render(request, 'analysis/cmdline.html', {'case':case,'cmd_list':list_data['rows']})

def gui(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = os.popen('cd analysis/templates/analysis/memory && ls '+case.c_owner.username+'_'+case.c_name+'_screenshots/*.png').read().split("\n")
	new_list = [i for i in list_data if  len(i)>4]
	#return
	return render(request, 'analysis/screens.html', {'case':case,'screens_list':new_list})

def mal(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'malfind')
	#return
	return render(request, 'analysis/malware.html', {'case':case,'malware_list':list_data['rows']})

def yara(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'yarascan')
	#return
	return render(request, 'analysis/yara.html', {'case':case,'yara_list':list_data['rows']})

def hashs(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = get_list_data(case, 'hashdump')
	#return
	return render(request, 'analysis/hashs.html', {'case':case,'hashs_list':list_data['rows']})

def mkatz(request):
	#TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	#end test cases#
	#get data
	list_data = open('analysis/templates/analysis/memory/'+case.c_owner.username+'_'+case.c_name+'_'+'mimikatz'+'.txt').read()
	#return
	return render(request, 'analysis/mkatz.html', {'case':case,'pass':list_data})

def proc_dump(request, p):
	# TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	# end test cases#
	list_data = get_list_data(case, 'init')
	profile_name = (str(list_data['rows'][0][0]).split(','))[0]
	script.pid_dump(case.c_file, profile_name, p)
	file_name = 'executable.'+p+'.exe'
	return redirect('/files/'+file_name)

def file_dump(request, Q):
	# TEST CASES :3#
	cookie = request.COOKIES.get('CID')
	if not cookie:
		return render(request, 'analysis/404.html')
	case = get_object_or_404(Case, c_fingerprint=cookie)
	if not request.user.is_authenticated:
		return redirect('list:login_user')
	if not case.c_owner == request.user:
		return render(request, 'analysis/404.html')
	# end test cases#
	list_data = get_list_data(case, 'init')
	profile_name = (str(list_data['rows'][0][0]).split(','))[0]
	script.f_dump(case.c_file, profile_name, Q)
	file_name = hex(int(Q))
	return redirect('/files/'+file_name)


################################################################END MEMORY

def err(request):
	return render(request, 'analysis/404.html')
