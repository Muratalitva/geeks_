from django.shortcuts import render
from settings.models import Index, About, Blog
# Create your views here.

def index(request):
    settings = Index.objects.all()

    return render(request, "index.html", locals())