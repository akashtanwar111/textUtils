#  I have created this file-Akash

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
     

def analyze(request):
    
    djtext= request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    print(removepunc)
    print(djtext)

    if removepunc == "on":
    
       punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed=""
       for char in djtext:
           if char not in punctuations:
               analyzed=analyzed+char
       params={'purpose':'remove punctuations','analyzed_text': analyzed}
       djtext=analyzed
    

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            
        params={'purpose':'change to Uppercase','analyzed_text': analyzed}
        djtext=analyzed
       
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed=analyzed+char
            
        params={'purpose':'removed new line','analyzed_text': analyzed}
        djtext=analyzed
      
    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate( djtext):
            if not( djtext [index]==" "and djtext[index+1]==" "):
               analyzed=analyzed+char
            
        params={'purpose':'removed new line','analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps !="on"):
        return HttpResponse("please select atleast one operation")

    return render(request,'analyze.html',params)
    