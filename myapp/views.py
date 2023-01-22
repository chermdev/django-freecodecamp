from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Bob',
        'age': '53',
        'nationality': 'British'
    }
    return render(request, "index.html", context)


def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
