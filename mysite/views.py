from django.http import HttpResponse
import datetime


def current_datetime(request):
    dt = datetime.datetime.now()
    html = "<html><body> It is %s now. </body></html>" %(dt)
    return HttpResponse(html)



def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> After %s hour(s),<br/> it will be %s. </body></html>" %(offset, dt)
    return HttpResponse(html)
