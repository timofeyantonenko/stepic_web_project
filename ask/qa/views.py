from django.http import HttpResponse, HttpResponseNotFound
def test(request, *args, **kwargs):
    if len(args)> 0 or bool(kwargs):
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('404 error')