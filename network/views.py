from django.shortcuts import render, redirect, get_object_or_404
from list.models import Case


def network(request):
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
    # capinfos
    list_data = open('network/templates/network/' + case.c_owner.username + '_' + case.c_name + '_' + 'capinfos.txt').read()
    lines = list_data.splitlines()
    l = []
    l.append([lines[5].split(':')[1], lines[6].split(':')[1], lines[9].split(':',1)[1], lines[10].split(':',1)[1], lines[11].split(':')[1]])
    return render(request, 'network_index.html', {'case': case, 'list': l[0]})


def file_dumps(request):
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
    list_data = open('network/templates/network/' + case.c_owner.username + '_' + case.c_name + '_' + 'tcpxtract.txt').read()
    lines = list_data.splitlines()
    list = []
    for line in lines:
        list.append([line.split('files/')[1],line.split(',')[0]])
    return render(request, 'file_dump.html', {'files':list})


def http_traffic(request):
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
    name = 'network/' + case.c_owner.username + '_' + case.c_name + '_' + 'captipper.html'
    return render(request, 'http_traffic.html', {'name':name})
