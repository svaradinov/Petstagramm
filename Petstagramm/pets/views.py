from django.shortcuts import render, redirect

from Petstagramm.pets.forms import PetForm
from Petstagramm.pets.models import Pet, Like


def list_pets(req):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(req, 'pet_list.html', context)

def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()

    context = {
        'pet': pet,
    }

    return render( req, 'pet_detail.html', context )

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

        return render(req, 'pet_create.html', context)

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

        return render(req, 'pet_create.html', context)