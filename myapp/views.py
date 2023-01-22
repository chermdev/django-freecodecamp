from django.shortcuts import render
from .models import Feature

# Create your views here.


def index(request):
    features = []
    feature_data = (('Fast', 'Lorem ipsum dolor sit amet.', True),
                    ('Reliable', 'Lorem ipsum dolor sit amet.', True),
                    ('Easy to Use', 'Lorem ipsum dolor sit amet.', False),
                    ('Affordable', 'Lorem ipsum dolor sit amet.', True))
    for name, details, is_true in feature_data:
        features.append(
            Feature(id=0,
                    name=name,
                    details=details,
                    is_true=is_true
                    )
        )
    context = {
        'features': features
    }
    return render(request, "index.html", context)


def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
