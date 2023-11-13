from django.shortcuts import render

# Create your views here.
def error404(request,exception):
    template_name = 'error/error404.html'
    print(exception)
    return render (request,template_name)