from re import I
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    ftext=request.POST.get('textutil', 'default')
    remove=request.POST.get('remove', 'off')
    upper=request.POST.get('upper', 'off')
    count=request.POST.get('count', 'off')
    ann=""
    cou=""
    if remove == 'on':
        puntuations='''!@#$%^&*(){}[]"',.?<>'''
        analyzed=""
        for char in ftext:
            if char not in puntuations:
                analyzed=analyzed+char
            params={'final': analyzed, 'purpose':'Removed Puntuations', 'Txtcount':''}
            ftext=analyzed
            ann="Removed Puntuations "
    
    if upper == 'on':
        analyzed=""
        for char in ftext:
            analyzed=analyzed+char.upper()
        params={'final': analyzed, 'purpose':'Removed Puntuations', 'Txtcount':''}
        if remove == 'on':
            ftext=analyzed
            ann=ann+"And UpperCased"
        else:
            ftext=analyzed
            ann="UpperCased"

    if count == 'on':
        i=0
        for char in ftext:
            i=i+1
        params={'final': ftext, 'purpose':'Counted', 'Txtcount':i}
        cou="text count : "+str(i)


    params={'final': analyzed, 'purpose':ann, 'Txtcount':cou}
    return render(request, 'analyze.html', params)