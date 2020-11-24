from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import RecipesForm
from .models import RecipesName


def home(request):
    data = RecipesName.objects.order_by('recipe')
    return render(request, "recipesapp/home.html", {'data': data})


def creatobj(request):
    if request.method == 'POST':
        objcreate = RecipesForm(request.POST)
        if objcreate.is_valid():
            recipe = request.POST.get('recipe', '')
            items = request.POST.get('items','')
            making = request.POST.get('making', '')
            objdata = RecipesName(
                recipe= recipe,
                items= items,
                making =making,)
            objdata.save()
            return  redirect('/home')
        else:
            return HttpResponse('data invalid')
    else:
        objcreate = RecipesForm()
        return render(request, "recipesapp/create.html", {'form': objcreate})


def delete(request, id):
    data = get_object_or_404(RecipesName,pk=id)
    data.delete()
    return redirect('/home')


def details(request, id):
    data = get_object_or_404(RecipesName, pk=id)
    return render(request, "recipesapp/details.html",{'data': data})