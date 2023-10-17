from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "app_hw_web10/index.html", context={"title": "Web 10 hw!"})
