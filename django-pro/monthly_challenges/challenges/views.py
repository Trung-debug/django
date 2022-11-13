from types import NoneType
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
"""
Create some basic functions to render string by HttpResponse
"""
# def january(request):
#     return HttpResponse("First Views and Urls")

# def february(reuquest):
#     return HttpResponse("Python is awsome")

# def march(request):
#     return HttpResponse("Learn Django at least 20 minutes everyday")


"""
create the Url with short method
"""

# def monthly_challenges(request, month):
#     challenge_text = None
#     if month == "January":
#         challenge_text = "First Views and Urls"
#     elif month == "February":
#         challenge_text = "Python is awsome"
#     elif month == "March":
#         challenge_text = "Learn Django at least 20 minutes everyday"
#     else:
#         return HttpResponseNotFound("404 ERROR PAGE NOT FOUND!")
#     return HttpResponse(challenge_text)

##########################################################################


"""
Create the Url with the List and replace the if else method
"""
monthly_challenges_12months = {
    "january" : "The first Url",
    "february" : "The second Url",
    "march" : "The third Url ",
    "april" : "The fourth Url",
    "may" : "The fifth Url",
    "june" : "The sixth Url",
    "july" : "The seventh Url",
    "august" : "The eighth Url",
    "september" : "The nineth Url",
    "october" : "The tenth Url",
    "november" : "The eleventh Url",
    "december" : None
}

# def index(request):
#     list_item = ""
#     months = list(monthly_challenges_12months.keys())
#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("month_challenge", args=[month])
#         list_item += f"<li> <a href =\"{month_path}\">{capitalized_month}</a> </li>"

#     #"<li><a href = \"...\">January</a></li>"
#     response_data =f"<ul>{list_item}</ul>" 

#     return HttpResponse(response_data)
def index(request):
    list_item = ""
    months = list(monthly_challenges_12months.keys())
    return render(request, "challenges/index.html",{
        "months": months,
    })

def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenges_12months[month]
        # response_data = f"<h1>{challenges_text}</h1>"
        response_data = render_to_string("challenges/challenge.html",{
            "text" : challenges_text,
            # "month_name" : month.capitalize()
            "month_name" : month
        })
        return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


"""
Create a redirect month
Note create a variable that can store the list
"""
def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_12months.keys())

    if month > len(months):
        return HttpResponseNotFound("404 page NOT Found")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month]) #return path /challenges/<month>
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)