## Instead of all these
#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse

## What we can do?
from django.shortcuts import render_to_response
import datetime


def current_datetime(request):
    now = datetime.datetime.now()        
    ## Good
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
	#return HttpResponse(html)

	## Better
    return render_to_response('current_datetime.html', {'current_date':now})

    ## Best
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> After %d hour(s),<br/> it will be %s. </body></html>" %(offset, dt)
    return HttpResponse(html)