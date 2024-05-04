
import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .utils import retrieve, retrieve_all_data

# Create your views here.
def dashboard(request):
    return render(request, 'core/main_dashboard.html')

def retrieve_loadCurve(request):
    data = retrieve('VoltageA', 'VoltageB', 'VoltageC')
    return JsonResponse(data, safe=False)

def retrieve_threePhaseCurrent(request):
    data = retrieve('CurrentA', 'CurrentB', 'CurrentC')
    return JsonResponse(data, safe=False)

def loadCurveDashboard(request):
    return render(request, 'core/main_dashboard.html', {'loadCurveOnly':True})

def threePhaseCurrentDashboard(request):
    return render(request, 'core/main_dashboard.html', {'threePhaseCurrentOnly':True})

def retrieve_all(request):
    return JsonResponse(retrieve_all_data())

def post_request(request):
    endpoint = "https://script.google.com/macros/s/AKfycbyPIWSjHUbEd1ZqNY7Zfe0Syzt_XJWCf9O8oGFEr-xPFjiqEOYfsmQi1ud0nHDgMAfHBg/exec?sts=write&VphaseA=130.0175&VphaseB=1200.46&VphaseC=1259.45&current_Ia=98.7&current_Ib=99.45&current_Ic=97.11&app_power=1000&real_power=800&react_power=600&pf=0.99"
    response = requests.post(endpoint)
    return HttpResponse("Response COmplete")