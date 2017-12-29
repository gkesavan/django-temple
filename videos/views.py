from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import fileDetails, tvDetails
from datetime import date
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.


def videoloop(request):
    return render(request, 'videos/index.html', {})

def videoloopbytv(request, tvid):
    print(tvid)
    listoftvs = []
    all_tvs = tvDetails.objects.all()
    for tv in all_tvs:
        listoftvs.append(tv.tv_name.lower())

    if tvid.lower() in listoftvs:
        return render(request, 'videos/bytv.html', {})
    else:
        return redirect('/temple/tv/TV-Default')


def imageloop(request):
    return render(request, 'videos/imageloop.html', {})

@csrf_exempt
def getvideolist(request):
    results = []
    # file1 = 'C:\\Users\\ujalagam\\templevideo\\temple\\videos\\static\\videos\\files\\videos.txt'
    # with open(file1) as fs:
    #     results = []
    #     alllines = fs.read()
    #     alllines = alllines.split('\n')
    #     for line in alllines:
    #         results.append(line)
    all_instaces = fileDetails.objects.all()
    for inst in all_instaces:
        if inst.play_from <= date.today() <= inst.play_Till:
            results.append(str(inst.file_path) + ":" + inst.filetype + ":" + str(inst.play_duration))
        else:
            print("From Time : ", inst.play_from)
    return JsonResponse({"fileslist": results})


@csrf_exempt
def getmediadetailsbytvid(request, tvid):
    results = []
    print("TV ID is :" + tvid)
    # tvid = request.POST.get("tvid", "")
    all_instaces = fileDetails.objects.all()   #.filter(play_on_tv_id = tvid )
    for inst in all_instaces:
        print(inst.play_on_tv_id.lower())
        if tvid.lower() == inst.play_on_tv_id.lower():
            if inst.play_from <= date.today() <= inst.play_Till:
                results.append(str(inst.file_path) + ":" + inst.filetype + ":" + str(inst.play_duration))
            else:
                print("From Time : ", inst.play_from)
    return JsonResponse({"fileslist": results})

@csrf_exempt
def getlistofimages(request):
    listofimages = [f.name for f in os.scandir('C:\\temple\\templevideo\\images') if f.is_file()]
    return JsonResponse({"imagelist": listofimages})

