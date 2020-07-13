from django.shortcuts import render, redirect, get_object_or_404
from list.models import Case


def disk(request):
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
    return render(request, 'disk_index.html', {'case': case})


def dumped_files(request):
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
    list_data = open('disk/templates/disk/' + case.c_owner.username + '_' + case.c_name + '_' + 'binwalk.txt').read()
    list_data = list_data.split('-\n')[1]
    list_data = list_data.splitlines()
    l = []
    for i in list_data:
        l.append(i.split('      '))

    return render(request, 'dumped.html', {'data': l})


def deleted_files(request):
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
    list_data = open('disk/templates/disk/' + case.c_owner.username + '_' + case.c_name + '_' + 'binwalk.txt').read()
    list_data = list_data.split('-\n')[1]
    list_data = list_data.splitlines()

    return render(request, 'dumped.html', {'data': list_data})
