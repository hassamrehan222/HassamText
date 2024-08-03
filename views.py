from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ex1(request):
    s = ''' <h1>Social Media Bar<br></h1>

                  <a href = "https://www.facebook.com/profile.php?id=100085131734103"> Em soha editx</a><br>
                  <a href = " https://en.wikipedia.org/wiki/Kurulu%C5%9F:_Osman" >Kurulus Osman</a><br>
                  <a href = "https://www.instagram.com/"> Instagram</a><br>
                  <a href = "https://www.coursera.org/courses?query=python"> python cource</a><br>'''
    return HttpResponse(s)

def analyze(request):
    djtext = request.POST.get('text', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
   
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    return render(request, 'analyze.html', params)
