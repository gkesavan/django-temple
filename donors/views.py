from django.shortcuts import render
from django.http import JsonResponse
#from django.template import template


from datetime import date
from .models import details
from videos.models import tvDetails

def getdonorstoday(request):
    results = []
    donors = details.objects.all()
    tvdetails = tvDetails.objects.all()
   # t = template.loader.get_template('donors/index.html')

    for donor in donors:
        print('inide for')
        print(str(donor.display_until)+" <= " +str(date.today()) +" <= " +str(donor.display_from))
        today = date.today()
        if donor.display_until >= today >= donor.display_from:
           for tv in tvdetails:
               if tv.tv_name == donor.display_on_tv_id:
                   results.append({"name": donor.display_name,
                       "tv_location": tv.tv_location })
    #return JsonResponse({"donors":results})
    print(results)
    return render(request, 'donors/index.html', {'donors':results})

