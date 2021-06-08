from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def submittedInfo (request):
    print(request.POST)
    context = {
        'name': request.POST['yourname'],
        'dojo': request.POST['dojolocation'],
        'lang': request.POST['favoritelanguage'],
        'comment': request.POST['comment']
    }
    return render(request, 'info.html', context)


def root(request):
    return redirect('/')