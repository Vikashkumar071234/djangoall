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
   
    fruits = ['Apple','mango','Guava','Banana']
    return render(request,"index.html",context={'peoples':peoples,'text':text,'fruits':fruits,'page':'Django course'})
    # return HttpResponse("""<h1>Vikash</h1>
    #                     <hr>
    # <p>Vikash Singh</p>
                        
    # """)
    

def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)


def contact(request):
    context={'page':'contact'}
    return render(request,"contact.html",context)

def success_page(request):
    return HttpResponse("<h1>Singh</h1>")

def index(request):
    return render(request,'index.html')