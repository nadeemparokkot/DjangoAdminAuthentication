from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo
from . forms import MovieForm

# Create your views here.
def print_create(request):
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid():
           frm.save()
    else:
        frm=MovieForm()
    return render(request,'create.html',{'frm':frm})
    

def print_list(request):
    retrive_data=MovieInfo.objects.all()
    # print(retrive_data) 
    return render(request,'list.html',{'movie':retrive_data})



def print_edit(request,pk):
    edit_instance=MovieInfo.objects.get(pk=pk)
    frm=MovieForm(instance=edit_instance)
    if request.POST:
        #frm=MovieForm(request.POST,instance=edit_instance)
        #if frm.is_valid():
         #   edit_instance.save()
    #else:
        #    frm=MovieForm(instance=edit_instance)  method ===2
        title=request.POST.get('head') #head date and description are from datamodel
        year=request.POST.get('date')
        summary=request.POST.get('descrption')
        
        edit_instance.head=title
        edit_instance.date=year
        edit_instance.descrption=summary
        
        edit_instance.save()
    return render(request,'create.html',{'frm':frm})



def print_delete(request,pk):
    delete_instance=MovieInfo.objects.get(pk=pk)
    delete_instance.delete()
    retrive_data=MovieInfo.objects.all()
   
    return render(request,'list.html',{'movie':retrive_data})