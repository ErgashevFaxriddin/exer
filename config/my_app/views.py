from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    html = """
    <h1>First page</h1>
    """
    return HttpResponse(html)