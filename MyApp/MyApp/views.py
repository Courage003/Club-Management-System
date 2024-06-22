from django.http import HttpResponse
from django.shortcuts import render

import datetime
def home(request):
    isActive=True
    if request.method=='GET':

        check= request.GET.get("check")
        print(check)

        if check is None: isActive=False
        else: isActive=True


    date=datetime.datetime.now()
    
    name="Mowgli Vloggers"
    list_of_companies=[
        'Google',
        'Microsoft',
        'Oracle',
        'Cisco'
    ]
    student={
        'student_name': "Dhruv",
        'student_college': "NIT Agartala",
        'student_city': "AGRA"
    }

    data={
        'date': date,
        'isActive':isActive,
        'name':name,
        'list_of_companies': list_of_companies,
        'student_data': student
        
    }
    #print("Test function is called from view")
    #return HttpResponse("<h1>Hello this is index page</h1>")
    return render(request, "home.html", data)

def about(request):
    #return HttpResponse("This is about page")
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})

