from django.shortcuts import render
from .models import chien, chat, oiseau
from .forms import AdoptionForm, ContactForm


def get_accueil(request):
    return render(request, 'accueil.html')

def get_typeAnimal(request,slug):
    if slug == 'chat':
        animals = chat.objects.all
    elif slug == 'chien':
        animals = chien.objects.all
    elif slug == 'oiseau':
        animals = oiseau.objects.all
    
    return render(request,'typeAnimal.html',{'animals':animals,'slug':slug})

def get_adoptationForm(request,slug1,slug2):
    type_page = 'Valide'
    if slug1 == 'chat':
        count = chat.objects.all().count()
        for a in range(count):
            animal = chat.objects.get(id=a+1)
            if slug2 == animal.nom:
                if request.method == "POST":
                    form = AdoptionForm(request.POST)
                    if form.is_valid():
                        return render(request,'adoptationForm.html',{'type':type_page})
                else:
                    type_page = 'Adoption'
                    form = AdoptionForm()
                    return render(request,'adoptationForm.html',{'type':type_page,'form':form,'nom':slug2,'type1':slug1})
    elif slug1 == 'chien':
        count = chien.objects.all().count()
        for a in range(count):
            animal = chien.objects.get(id=a+1)
            if slug2 == animal.nom:
                if request.method == "POST":
                    form = AdoptionForm(request.POST)
                    if form.is_valid():
                        return render(request,'adoptationForm.html',{'type':type_page})
                else:
                    type_page = 'Adoption'
                    form = AdoptionForm()
                    return render(request,'adoptationForm.html',{'type':type_page,'form':form,'nom':slug2,'type1':slug1})
    elif slug1 == 'oiseau':
        count = oiseau.objects.all().count()
        for a in range(count):
            animal = oiseau.objects.get(id=a+1)
            if slug2 == animal.nom:
                if request.method == "POST":
                    form = AdoptionForm(request.POST)
                    if form.is_valid():
                        return render(request,'adoptationForm.html',{'type':type_page})
                else:
                    type_page = 'Adoption'
                    form = AdoptionForm()
                    return render(request,'adoptationForm.html',{'type':type_page,'form':form,'nom':slug2,'type1':slug1})
            
def get_contact(request):
    type_page = 'thanks'
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request,'contactForm.html',{'type':type_page})
    else:
        type_page = 'contact'
        form = ContactForm()
    
    return render(request,'contactForm.html',{'type':type_page, 'form':form})