from django.http import HttpResponse
from django.shortcuts import render

def new(request):
    return render(request, 'new.html')

def index(request):

    return render(request, 'index.html') 

def removepunc(request):
    mytext=request.POST.get('text', 'default')
    repu= request.POST.get('removepunc', 'off')
    caps= request.POST.get('fullcaps', 'off')
    chco= request.POST.get('charcount', 'off')
    if repu == "on":
        analyse =  ""
        punctuations = '''!()-{}[];:'"\/,.<>?@#$%^&*_~'''
        for char in mytext:
            if char not in punctuations:
                analyse += char
        params={'purpose':'removepunc', 'Analyzed_text': analyse}
        mytext=analyse
    if caps == "on":
        analyse = ""
        for char in mytext:
            analyse += char.upper()
        params={'purpose':'Full capitalized', 'Analyzed_text': analyse}
        mytext=analyse
    if chco == "on":
        analyse = 0
        for char in mytext:
            analyse+=1
        params={'purpose':'character count', 'Analyzed_text': analyse}
        mytext=analyse

    return render(request, 'analyze.html', params)