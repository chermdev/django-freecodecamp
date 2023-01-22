from django.shortcuts import render
from .models import Feature


# Create your views here.
def index(request):

    features = Feature.objects.all()
    feature_data = (('Easy to Use', 'Lorem ipsum dolor sit amet.'),
                    ('Affordable', 'Lorem ipsum dolor sit amet.'))
    return render(request, "index.html", {'features': features})


def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
