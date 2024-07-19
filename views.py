from django.shortcuts import render, redirect
from .models import Obituary
from django.utils.text import slugify
from django.db import DatabaseError

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        
        # Create a unique slug for the obituary
        slug = slugify(name + "-" + str(date_of_death))
        
        # Create an Obituary instance and save it to the database
        try:
            obituary = Obituary(
                name=name,
                date_of_birth=date_of_birth,
                date_of_death=date_of_death,
                content=content,
                author=author,
                slug=slug
            )
            obituary.save()
            # Redirect to a confirmation page or another view
            return redirect('confirmation')  # Adjust this to point to your confirmation view
        except DatabaseError:
            # Handle the error (e.g., log it, show an error message)
            return render(request, 'obituary_form.html', {
                'error': 'An error occurred while submitting the obituary. Please try again.'
            })
        
    return render(request, 'obituary_form.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
