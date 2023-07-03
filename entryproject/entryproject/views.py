from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('<h3>hello world!</h3>')