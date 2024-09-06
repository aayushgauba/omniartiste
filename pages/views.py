from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def sitemap(request):
    return HttpResponse(open('templates/sitemap.xml').read(), content_type='text/xml')