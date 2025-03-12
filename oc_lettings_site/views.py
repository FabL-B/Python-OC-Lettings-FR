from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def custom_404(request, exception):
    """Display 404 error"""
    return render(request, "404.html", status=404)

def custom_500(request):
    """Display 500 error"""
    return render(request, "500.html", status=500)
