from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from . import models
from .forms import ProduitForm, CategorieForm
# Create your views here.
def home(request):
    data = models.Produit.objects.all().order_by('-pk')  
    return render(request, 'application/home.html', {'data':data})

def post_new(request):
    if request.method=="POST":
        form=ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save()
            return redirect('home')
    else:
        form=ProduitForm()
    return render(request, 'application/formulaire.html', {'form':form})

def update(request, id):
    produit=models.Produit.objects.all
    data=models.Produit.objects.get(pk=id)
    form= ProduitForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        post=form.save(commit= False)
        post.save()
        return redirect('home')
          
    return render(request, 'application/modification.html', {'form':form, 'data':data})


def detail(request, id):
    detail=models.Produit.objects.get(pk=id)
#    detail2=models.Categorie.objects.get(pk=id)
    return render(request, 'application/detail.html', {'detail':detail})

def delete(request, id):
    delete1=models.Produit.objects.get(pk=id)
    delete1.delete()
    return redirect('home')
