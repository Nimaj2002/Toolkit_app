from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_index(requests):
    return render(requests, "index.html")