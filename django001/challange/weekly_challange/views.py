from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_challanges = {
    "monday":"Walk for 10 minutes",
    "tuesday":"walk for 20 minutes",
    "wednesday":"walk for 30 minutes",
    "thursday":"walk for 40 minutes",
    "friday":"walk for 50 minutes",
    "saturday":"walk for 60 minutes",
    "sunday":"walk for 70 minutes"
}

def Challange_by_no(request , day):
    if len(week_challanges)<day:
        return HttpResponseNotFound("Invalid")
    
    day_name = list(week_challanges.keys())[day]
    redirect_path = reverse("month-challange",args=[day_name])
    return HttpResponseRedirect(redirect_path)


    


def Challange_by_name(request , day):
    challange = None
    try:
        challange = f"<h1>{week_challanges[day]}"
    except:
        challange = "<h1>Invalid Challange</h1>"
        
    return HttpResponse(challange)
    

def index(request):
    list_items = ""
    days = list(week_challanges.keys())
    for day in days:
        day_path = reverse("week-challange",args=[day])
        list_items+=f"<li><a href='{day_path}'>{day.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)