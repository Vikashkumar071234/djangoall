from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
#function based view

def home(request):
    peoples=[
        {'name':'Vikash','age':'20'},
        {'name':'Rajesh','age':'30'},
        {'name':'Akshat','age':'23'},
    ]
    text="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis, amet numquam mollitia repellat iusto dolorem ab consequatur saepe assumenda hic veritatis vero consequuntur?"""
   
 
    return render(request,"index.html",context={'peoples':peoples,'text':text})
    # return HttpResponse("""<h1>Vikash</h1>
    #                     <hr>
    # <p>Vikash Singh</p>
                        
    # """)
    



def success_page(request):
    return HttpResponse("<h1>Singh</h1>")

def index(request):
    return render(request,'index.html')