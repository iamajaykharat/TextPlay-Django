# I created this file - Ajay
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get text here
    djtext = request.POST.get('text', 'default')
    # Check Checkbox here
    rp = request.POST.get('removepunc', 'off')
    uc = request.POST.get('uppercase', 'off')
    lc = request.POST.get('lowercase', 'off')
    nlr = request.POST.get('newlineremove', 'off')
    sr = request.POST.get('spaceremove', 'off')
    cc = request.POST.get('charcount', 'off')
    nr = request.POST.get('numberremover', 'off')
    per = ""

    # Punctuation remove
    if rp == 'on':
        analyzed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed += char
        p = {'per': 'Remove Punctuation', 'analysed_text': analyzed, 'total': ""}
        per += '| Remove Punctuation'
        djtext = analyzed
        tot = ''

    # Make uppercase
    if uc == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        p = {'per': 'Make Uppercase', 'analysed_text': analyzed, 'total': ""}
        per += '| Make Uppercase'
        djtext = analyzed
        tot = ''

    # Make lowercase
    if lc == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.lower()
        p = {'per': 'Make Lowercase', 'analysed_text': analyzed, 'total': ""}
        per += '| Make Lowercase'
        djtext = analyzed
        tot = ''

    # Newline Remove
    if nlr == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        p = {'per': 'Remove Newline', 'analysed_text': analyzed, 'total': ""}
        per += '| Remove Newline'
        djtext = analyzed
        tot = ''

    # Space Remove
    if sr == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        p = {'per': 'Remove Extra Spaces', 'analysed_text': analyzed, 'total': ""}
        per += '| Remove Extra Spaces'
        djtext = analyzed
        tot = ''

    # Number Remove
    if nr == "on":
        analyzed = ""
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        p = {'per': 'Remove Numbers', 'analysed_text': analyzed, 'total': ""}
        per += '| Remove Numbers'
        djtext = analyzed
        tot = ''

    # Count characters
    if cc == 'on':
        to = 0
        for char in djtext:
            if char != " ":
                to += 1
        analyzed = djtext
        tot = 'Total Characters: ' + str(to)
        p = {'per': 'Count All Characters', 'analysed_text': analyzed, 'total': tot}
        per += '| Count All Characters'

    if rp != 'on' and uc != 'on' and nlr != 'on' and sr != 'on' and cc != 'on'and lc != 'on' and nr != 'on':
        return HttpResponse("ERROR,Please select proper operation")

    p = {'per': per, 'analysed_text': analyzed, 'total': tot}
    return render(request, 'analyze.html', p)
