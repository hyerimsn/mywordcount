from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    text = request.GET["mytext"]
    a = text.split(" ")
    b = {}

    for i in a:
        if i in b:
            b[i] +=1
        else:
            b[i] = 1
    context = {'original':text, 'countdict':b, 'countitem':b.items}

    return render(request, 'result.html', context)
    