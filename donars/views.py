from django.shortcuts import render
from django.http import JsonResponse

from datetime import date
from .models import details
from videos.models import tvDetails

def getdonarstoday(request):
    results = []
    donars = details.objects.all()
    tvdetails = tvDetails.objects.all()
    print(tvdetails)
    for donar in donars:
        print(str(donar.display_until)+" <= " +str(date.today()) +" <= " +str(donar.display_from))
        today = date.today()
        if donar.display_until >= today >= donar.display_from:
           for tv in tvdetails:
               if tv.tv_name == donar.display_on_tv_id:
                   results.append({"name": donar.display_name,
                       "tv_location": tv.tv_location })
    return JsonResponse({"donars":results})
