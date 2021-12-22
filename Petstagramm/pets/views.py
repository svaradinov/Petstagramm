from django.shortcuts import render, redirect
from django.views.generic import ListView

from Petstagramm.pets.forms import PetForm
from Petstagramm.pets.models import Pet, Like


def list_pets(req):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(req, 'pets/pet_list.html', context)

class ListPetView(ListView):
    template_name = 'pets/pet_list.html'
    model = Pet
    context_object_name = 'pets'

def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()

    context = {
        'pet': pet,
    }

    return render(req, 'pets/pet_detail.html', context)

def like_pet(req, pk):
    pet_to_like = Pet.objects.get(pk=pk)

    like = Like(pet=pet_to_like)

    like.save()

    return redirect('pet details', pet_to_like.id)


def create_pet(req):
    if req.method == 'POST':
        form = PetForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm()

        context = {
            'form': form,
        }

        return render(req, 'pets/pet_create.html', context)

def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == 'POST':
        form = PetForm(req.POST, instance = pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm(instance=pet)

        context = {
            'form': form,
        }

        return render(req, 'pets/pet_create.html', context)