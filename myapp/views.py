from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services are very quick. OnGod'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service are always on point'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Afordable'
    feature3.details = 'Our services are very affordable compared to other retailers'
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Quality'
    feature4.details = 'We offer you only quality goods and services'
    return render(request, 'index.html', feature = [feature1, feature2, feature3, feature4])

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})