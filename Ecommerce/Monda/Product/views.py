from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # return HttpResponse("<h1>Fuck the world i am coming for you </h1>")
    return render(request, 'products/index.html', {"categorie": categories, "products": products})