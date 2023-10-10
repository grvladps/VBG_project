from django.shortcuts import render


def index_page(request):
    return render(request, "index.html")


def cabinet_page(request):
    return render(request, "cabinet.html")
